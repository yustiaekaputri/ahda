import contextlib
import importlib.util
import json
from pathlib import Path
import sqlite3
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('collector', ROOT/'ahda_collector.py')
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        c.initialize(self.root/'db.sqlite')
        self.db = c.connect(self.root/'db.sqlite')
        self.mapping = {'npsn':'NPSN','name':'Nama','regency':'Kabupaten','students_total':'Total','students_male':'L','students_female':'P'}
    def tearDown(self):
        self.db.close(); self.tmp.cleanup()
    def book(self, rows, name='test.xlsx', headers=None):
        w = openpyxl.Workbook(); ws=w.active;ws.title='Data'
        ws.append(headers or ['NPSN','Nama','Kabupaten','Total','L','P'])
        for row in rows:ws.append(row)
        path=self.root/name;w.save(path);w.close();return path
    def imp(self, rows, **kwargs):
        path=self.book(rows,kwargs.pop('name','test.xlsx'))
        return c.import_xlsx(self.db,path,'Data',self.mapping,2026,**kwargs)
    def draft(self):
        self.imp([['20515441','SMKN 1 BANDUNG','KAB. TULUNGAGUNG',10,4,6]])
        out=c.run_jobs(self.db);return out['results'][0]['draft_id']
    def test_no_accidental_database_creation_or_overwrite(self):
        with self.assertRaises(sqlite3.OperationalError):c.connect(self.root/'missing.sqlite')
        with self.assertRaises(FileExistsError):c.initialize(self.root/'db.sqlite')
        other=self.root/'other.sqlite';sqlite3.connect(other).close()
        with self.assertRaises(ValueError):c.connect(other)
    def test_resume_and_exact_replay(self):
        rows=[[str(10000000+i),'Sekolah '+str(i),'Kabupaten',10,4,6] for i in range(1,11)]
        p=self.book(rows)
        first=c.import_xlsx(self.db,p,'Data',self.mapping,2026,max_rows=3)
        self.assertEqual(first['status'],'paused')
        blocked=c.run_jobs(self.db)['results'][0];self.assertEqual(blocked['error'],'IMPORT_NOT_COMPLETE')
        final=c.import_xlsx(self.db,p,'Data',self.mapping,2026)
        self.assertEqual(final['rows_processed'],7)
        self.assertEqual(c.import_xlsx(self.db,p,'Data',self.mapping,2026)['rows_processed'],0)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM observations').fetchone()[0],10)
        c.run_jobs(self.db,10)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],10)
    def test_identity_conflict_and_same_name_distinct_npsn(self):
        self.imp([['10000001','Nama sama','A',1,1,0],['10000002','Nama sama','A',1,1,0],['10000001','Nama berbeda','B',1,1,0]])
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM schools').fetchone()[0],2)
        self.assertEqual(self.db.execute("SELECT conflict FROM schools WHERE npsn='10000001'").fetchone()[0],1)
        with self.assertRaisesRegex(ValueError,'IDENTITY_CONFLICT'):c.evidence_snapshot(self.db,'10000001')
    def test_invalid_counts_and_sum_not_published(self):
        self.imp([['10000001','Sekolah','A',100,2,3],['10000002','Sekolah','A',-1,2,3]])
        for code in ('10000001','10000002'):
            snap=c.evidence_snapshot(self.db,code)
            self.assertEqual(snap['statistics'],[])
            self.assertNotIn('peserta didik',c.template(snap)['article_text'])
    def test_conflicting_counts_withheld_across_files(self):
        self.imp([['10000001','Sekolah','A',10,4,6]])
        self.imp([['10000001','Sekolah','A',11,5,6]],name='second.xlsx')
        snap=c.evidence_snapshot(self.db,'10000001')
        self.assertEqual(snap['statistics'],[])
        self.assertEqual(snap['warnings'][0]['code'],'CONFLICTING_STUDENT_COUNTS')
    def test_duplicate_preserves_provenance_not_school_duplication(self):
        self.imp([['10000001','Sekolah','A',10,4,6]]*2)
        snap=c.evidence_snapshot(self.db,'10000001')
        self.assertEqual(len(snap['sources']),2);self.assertEqual(len(snap['statistics']),1)
        self.assertIn('DUPLICATE_NPSN_OBSERVATION',snap['sources'][1]['issues'])
    def test_formula_and_bad_npsn_quarantined(self):
        self.imp([['=1+1','Bad','A',1,1,0],['1e7','Bad','A',1,1,0],['10000001','Good','A','=2+2',1,0]])
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM schools').fetchone()[0],0)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM observations').fetchone()[0],3)
    def test_no_student_personal_columns_retained(self):
        p=self.book([['10000001','Sekolah','A',1,1,0,'PRIVATE STUDENT NAME']],headers=['NPSN','Nama','Kabupaten','Total','L','P','Nama Siswa'])
        c.import_xlsx(self.db,p,'Data',self.mapping,2026)
        self.assertNotIn('PRIVATE',self.db.execute('SELECT facts_json FROM observations').fetchone()[0])
    def test_plain_text_sql_injection_and_xss(self):
        self.imp([['10000001',"Sekolah '); DROP TABLE schools;--",'A',1,1,0],['10000002','<script>x</script>','A',1,1,0]])
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM schools').fetchone()[0],1)
        self.assertIn('DROP TABLE',c.template(c.evidence_snapshot(self.db,'10000001'))['article_text'])
    def test_pause_resume_and_expired_lease_fence(self):
        self.imp([['10000001','Sekolah','A',1,1,0]])
        c.control(self.db,'pause');self.assertEqual(c.run_jobs(self.db)['results'],[])
        c.control(self.db,'resume')
        with patch.object(c.time,'time',side_effect=[100,161]):out=c.run_jobs(self.db,1)
        self.assertEqual(out['results'][0]['error'],'LEASE_LOST')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],0)
        c.run_jobs(self.db,1);self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],1)
    def test_explicit_recovery_and_retry_bound(self):
        self.imp([['10000001','A','A',1,1,0],['10000001','B','A',1,1,0]])
        for _ in range(5):c.run_jobs(self.db,1)
        self.assertEqual(dict(self.db.execute('SELECT status,attempts FROM jobs').fetchone()),{'status':'failed','attempts':3})
        c.control(self.db,'retry-failed');self.assertEqual(self.db.execute('SELECT attempts FROM jobs').fetchone()[0],0)
        with self.db:self.db.execute("UPDATE jobs SET status='leased',token='x',leased_until=0")
        c.control(self.db,'recover');self.assertIsNone(self.db.execute('SELECT token FROM jobs').fetchone()[0])
    def test_immutable_cache_replay(self):
        draft=self.draft();payload=self.db.execute('SELECT payload FROM drafts').fetchone()[0]
        with self.db:self.db.execute("UPDATE jobs SET status='queued'")
        # Existing immutable cache is replayed, never overwritten.
        c.run_jobs(self.db,1)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],1)
        self.assertEqual(self.db.execute('SELECT payload FROM drafts').fetchone()[0],payload)
    def test_sql_fault_rolls_back_draft_and_checkpoint(self):
        self.imp([['10000001','A','A',1,1,0]])
        with self.db:self.db.execute("CREATE TRIGGER fail_draft BEFORE INSERT ON drafts BEGIN SELECT RAISE(ABORT,'synthetic fault'); END")
        result=c.run_jobs(self.db,1)
        self.assertEqual(result['results'][0]['error'],'INTERNAL_ERROR')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],0)
        self.assertEqual(self.db.execute('SELECT status FROM jobs').fetchone()[0],'retry_wait')
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM audit WHERE event='draft_saved'").fetchone()[0],0)
        with self.db:self.db.execute('DROP TRIGGER fail_draft')
        c.run_jobs(self.db,1)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],1)
    def test_stale_worker_cannot_complete_replaced_lease(self):
        self.imp([['10000001','A','A',1,1,0]])
        original=c.template
        def replace(snapshot):
            with self.db:self.db.execute("UPDATE jobs SET token='new-owner' WHERE npsn='10000001'")
            return original(snapshot)
        with patch.object(c,'template',side_effect=replace):result=c.run_jobs(self.db,1)
        self.assertEqual(result['results'][0]['error'],'LEASE_LOST')
        self.assertEqual(self.db.execute('SELECT token FROM jobs').fetchone()[0],'new-owner')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],0)
    def test_input_change_before_commit_rejected(self):
        self.imp([['10000001','A','A',1,1,0]])
        original=c.template
        def change(snapshot):
            with self.db:self.db.execute("UPDATE schools SET identity_json=? WHERE npsn='10000001'",(c.canonical({'name':'B','regency':'A'}),))
            return original(snapshot)
        with patch.object(c,'template',side_effect=change):result=c.run_jobs(self.db,1)
        self.assertEqual(result['results'][0]['error'],'INPUT_CHANGED_RETRY')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0],0)
    def test_export_stale_rejected_and_existing_file_preserved(self):
        draft=self.draft();out=self.root/'draft.json';c.export_draft(self.db,draft,out)
        with self.assertRaises(FileExistsError):c.export_draft(self.db,draft,out)
        self.imp([['20515441','SMKN 1 BANDUNG','KAB. TULUNGAGUNG',12,6,6]],name='new.xlsx')
        with self.assertRaisesRegex(ValueError,'STALE_DRAFT'):c.export_draft(self.db,draft,self.root/'stale.json')
    def test_bad_mapping_and_duplicate_header(self):
        p=self.book([['10000001','Sekolah','A',1,1,0]])
        for mapping in ({'name':'Nama'},{'npsn':'NPSN','name':'Nama','student_name':'X'}):
            with self.assertRaises(ValueError):c.import_xlsx(self.db,p,'Data',mapping,2026)
        p=self.book([],headers=['NPSN','Nama','Nama'])
        with self.assertRaisesRegex(ValueError,'HEADER'):c.import_xlsx(self.db,p,'Data',{'npsn':'NPSN','name':'Nama'},2026)
    def test_issue_pagination_cli_and_report(self):
        self.imp([['10000001','A','A',-1,1,0],['10000002','B','B',5,1,0]])
        result=c.main(['--db',str(self.root/'db.sqlite'),'issues','--limit','1'])
        self.assertTrue(result['has_more']);self.assertEqual(len(result['entries']),1)
        next_page=c.main(['--db',str(self.root/'db.sqlite'),'issues','--limit','1','--after',str(result['cursor'])])
        self.assertFalse(next_page['has_more']);self.assertGreater(next_page['cursor'],result['cursor'])
        self.assertEqual(c.main(['--db',str(self.root/'db.sqlite'),'report'])['schools'],2)
    def test_xml_entities_are_blocked(self):
        import zipfile
        p=self.book([['10000001','A','A',1,1,0]])
        with zipfile.ZipFile(p) as z:entries={n:z.read(n) for n in z.namelist()}
        payload=b'<!DOCTYPE worksheet [<!ENTITY ext SYSTEM "file:///should-never-read">]><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1" t="inlineStr"><is><t>&ext;</t></is></c></row></sheetData></worksheet>'
        entries['xl/worksheets/sheet1.xml']=payload
        with zipfile.ZipFile(p,'w') as z:
            for name,raw in entries.items():z.writestr(name,raw)
        from defusedxml.common import DefusedXmlException
        with self.assertRaises(ValueError) as caught:c.import_xlsx(self.db,p,'Data',self.mapping,2026)
        self.assertIsInstance(caught.exception.__cause__,DefusedXmlException)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM schools').fetchone()[0],0)
    def test_source_reference_never_fetches(self):
        self.draft()
        self.assertFalse(c.add_source(self.db,'20515441','https://smknbandung.sch.id/','school_website')['source_verified'])
        for url in ('http://example.org','https://127.0.0.1/','https://a.local/','https://x@school.sch.id/','file:///etc/passwd'):
            with self.assertRaises(ValueError):c.url_reference(url)
    def test_ollama_is_optional_and_cannot_replace_facts(self):
        draft=self.draft();before=self.db.execute('SELECT payload FROM drafts').fetchone()[0]
        calls=[]
        def fake(prompt):calls.append(prompt);return 'Saran model yang belum diperiksa.'
        with self.assertRaisesRegex(ValueError,'CONSENT'):c.edit_ollama(self.db,draft,'NO',fake)
        result=c.edit_ollama(self.db,draft,'LOCAL_OLLAMA_EDIT',fake)
        self.assertEqual(len(calls),1);self.assertFalse(result['canonical_draft_replaced'])
        self.assertEqual(self.db.execute('SELECT payload FROM drafts').fetchone()[0],before)
        with self.assertRaises(ValueError):c.edit_ollama(self.db,draft,'LOCAL_OLLAMA_EDIT',lambda _: '<script>x</script>')
    def test_source_changed_during_import_quarantined(self):
        p=self.book([['10000001','Sekolah','A',1,1,0]])
        original=c.file_hash(p)
        with patch.object(c,'file_hash',side_effect=[original,'x'*64]):
            with self.assertRaisesRegex(ValueError,'SOURCE_CHANGED'):c.import_xlsx(self.db,p,'Data',self.mapping,2026)
        with self.assertRaisesRegex(ValueError,'IMPORT_NOT_COMPLETE'):c.evidence_snapshot(self.db,'10000001')

if __name__=='__main__':unittest.main()
