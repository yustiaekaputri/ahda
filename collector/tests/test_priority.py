import json
from pathlib import Path
import sqlite3
from unittest.mock import patch
import test_collector as base
c=base.c

# Own fixture setup, without inheriting/re-running the entire original suite.
import unittest
class PriorityTests(unittest.TestCase):
    setUp=base.CollectorTests.setUp
    tearDown=base.CollectorTests.tearDown
    book=base.CollectorTests.book
    def load(self, rows):
        p=self.book(rows,headers=['NPSN','Nama','Bentuk'])
        return c.import_xlsx(self.db,p,'Data',{'npsn':'NPSN','name':'Nama','school_form':'Bentuk'},2026)
    def old_schema(self):
        with self.db:
            self.db.execute('DROP INDEX jobs_ready_priority')
            self.db.execute('ALTER TABLE jobs RENAME TO jobs_v2')
            self.db.execute("CREATE TABLE jobs(npsn TEXT PRIMARY KEY REFERENCES schools(npsn),status TEXT NOT NULL DEFAULT 'queued',attempts INTEGER NOT NULL DEFAULT 0,token TEXT,leased_until INTEGER,error TEXT)")
            self.db.execute('INSERT INTO jobs SELECT npsn,status,attempts,token,leased_until,error FROM jobs_v2')
            self.db.execute('DROP TABLE jobs_v2');self.db.execute('PRAGMA user_version=1')
        self.db.close()
    def test_all_lower_secondary_first_even_when_npsn_larger(self):
        self.load([['10000001','SMA','SMA'],['10000002','MA','MA'],['10000009','MTs','MTs'],['10000008','SMP','SMP'],['10000003','SMK','SMK']])
        out=c.run_jobs(self.db,10)['results']
        self.assertEqual([x['npsn'] for x in out],['10000008','10000009','10000001','10000002','10000003'])
    def test_unknown_other_and_missing_excluded_by_default(self):
        self.load([['10000001','SMP in name only','SD'],['10000002','MTs in name only',None],['10000003','Multi-level','SLB']])
        self.assertEqual(c.run_jobs(self.db,10)['results'],[])
        self.assertEqual(len(c.run_jobs(self.db,10,include_other=True)['results']),3)
    def test_explicit_equivalents_and_case_normalization(self):
        for form in ['SMP',' mtS ','MTsN','SMPLB','SMPK','SMPTK','Paket B']:
            self.assertEqual(c.school_priority({'school_form':form}),0)
        for form in ['SMA','SMK','MA','MAN','MAK','SMALB','SMAK','SMTK','Paket C']:
            self.assertEqual(c.school_priority({'school_form':form}),1)
        for form in ['SLB','SD','TK','SMK-UNKNOWN',None]:
            self.assertEqual(c.school_priority({'name':'SMP','school_form':form}),2)
    def test_ready_queue_uses_partial_index(self):
        plan=self.db.execute("EXPLAIN QUERY PLAN SELECT * FROM jobs WHERE status IN ('queued','retry_wait') AND attempts<3 AND priority<=1 ORDER BY priority,npsn LIMIT 1").fetchall()
        text=' '.join(str(tuple(r)) for r in plan)
        self.assertIn('jobs_ready_priority',text);self.assertNotIn('TEMP B-TREE',text)
    def test_v1_explicit_upgrade_backup_and_cache_preserved(self):
        self.load([['10000001','SMP','SMP'],['10000002','SMA','SMA']]);c.run_jobs(self.db,1)
        before=self.db.execute('SELECT payload FROM drafts').fetchone()[0]
        self.old_schema()
        with self.assertRaises(ValueError):c.connect(self.root/'db.sqlite')
        out=c.upgrade(self.root/'db.sqlite');self.assertTrue(out['upgraded'])
        backup=sqlite3.connect(out['backup']);self.assertEqual(backup.execute('PRAGMA user_version').fetchone()[0],1);backup.close()
        self.db=c.connect(self.root/'db.sqlite')
        self.assertEqual(self.db.execute('SELECT payload FROM drafts').fetchone()[0],before)
        self.assertEqual([r[0] for r in self.db.execute('SELECT priority FROM jobs ORDER BY npsn')],[0,1])
        self.assertFalse(c.upgrade(self.root/'db.sqlite')['upgraded'])
    def test_upgrade_rejects_active_lease(self):
        self.load([['10000001','SMP','SMP']])
        with self.db:self.db.execute("UPDATE jobs SET status='leased',token='x',leased_until=9999999999")
        self.old_schema()
        with self.assertRaisesRegex(ValueError,'STOP_AND_RECOVER'):c.upgrade(self.root/'db.sqlite')
        self.assertFalse(Path(str(self.root/'db.sqlite')+'.before-priority-v2.sqlite').exists())
    def test_upgrade_failure_rolls_back_schema(self):
        self.load([['10000001','SMP','SMP']]);self.old_schema()
        with patch.object(c,'audit',side_effect=RuntimeError('synthetic failure')):
            with self.assertRaises(RuntimeError):c.upgrade(self.root/'db.sqlite')
        old=sqlite3.connect(self.root/'db.sqlite')
        self.assertEqual(old.execute('PRAGMA user_version').fetchone()[0],1)
        self.assertNotIn('priority',[r[1] for r in old.execute('PRAGMA table_info(jobs)')]);old.close()
    def test_inspect_only_returns_headers_not_private_rows(self):
        p=self.book([['10000001','PRIVATE ROW','SMP']],headers=['NPSN','Nama','Bentuk'])
        out=c.inspect_xlsx(p)
        self.assertNotIn('PRIVATE ROW',json.dumps(out))
        self.assertEqual(out['sheets'][0]['headers'],['NPSN','Nama','Bentuk'])
        self.assertEqual(out['data_rows_read'],0)
        self.assertEqual(c.main(['--db','unused','inspect-xlsx','--file',str(p)])['file_sha256'],out['file_sha256'])

    def shared_book(self, xml):
        import zipfile,re
        p=self.book([['10000001','PRIVATE ROW','SMP']],headers=['NPSN','Nama','Bentuk'])
        with zipfile.ZipFile(p) as z:entries={name:z.read(name) for name in z.namelist()}
        sheet=entries['xl/worksheets/sheet1.xml'].decode()
        sheet=re.sub(r'<row r="1">.*?</row>', '<row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="s"><v>1</v></c><c r="C1" t="s"><v>2</v></c></row>',sheet)
        entries['xl/worksheets/sheet1.xml']=sheet.encode();entries['xl/sharedStrings.xml']=xml
        with zipfile.ZipFile(p,'w') as z:
            for name,data in entries.items():z.writestr(name,data)
        return p
    def test_header_shared_strings_rich_text(self):
        xml=b'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><si><t>NPSN</t></si><si><r><t>Na</t></r><r><t>ma</t></r></si><si><t>Bentuk</t></si><si><t>PRIVATE STRING NOT NEEDED</t></si></sst>'
        p=self.shared_book(xml);out=c.inspect_xlsx(p)
        self.assertEqual(out['sheets'][0]['headers'],['NPSN','Nama','Bentuk'])
        self.assertNotIn('PRIVATE STRING',json.dumps(out))
    def test_header_shared_string_entity_rejected(self):
        from defusedxml.common import DefusedXmlException
        xml=b'<!DOCTYPE sst [<!ENTITY x SYSTEM "file:///not-permitted">]><sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><si><t>&x;</t></si></sst>'
        p=self.shared_book(xml)
        with self.assertRaises(DefusedXmlException):c.inspect_xlsx(p)
