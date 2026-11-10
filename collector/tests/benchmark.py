"""Synthetic local SQLite smoke scale, never WordPress/real school enrichment."""
import argparse
import importlib.util
import json
from pathlib import Path
import platform
import tempfile
import time
import openpyxl
spec=importlib.util.spec_from_file_location('collector',Path(__file__).resolve().parents[1]/'ahda_collector.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
p=argparse.ArgumentParser();p.add_argument('--rows',type=int,required=True);a=p.parse_args()
assert 1<=a.rows<=10000
with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);w=openpyxl.Workbook(write_only=True);s=w.create_sheet('Synthetic')
    s.append(['NPSN','Nama','Total','L','P'])
    for i in range(a.rows):s.append([str(10000000+i),'SYNTHETIC SCHOOL '+str(i),100,50,50])
    x=root/'fixture.xlsx';w.save(x);w.close();c.initialize(root/'test.sqlite');db=c.connect(root/'test.sqlite')
    start=time.monotonic()
    imp=c.import_xlsx(db,x,'Synthetic',{'npsn':'NPSN','name':'Nama','students_total':'Total','students_male':'L','students_female':'P'},2026)
    import_seconds=time.monotonic()-start;start=time.monotonic()
    while c.run_jobs(db,100)['results']:pass
    duration=time.monotonic()-start
    schools=db.execute('SELECT COUNT(*) FROM schools').fetchone()[0];drafts=db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0]
    assert schools==drafts==a.rows
    assert db.execute("SELECT COUNT(*) FROM jobs WHERE status!='complete'").fetchone()[0]==0
    before=drafts;c.run_jobs(db,100);assert db.execute('SELECT COUNT(*) FROM drafts').fetchone()[0]==before
    db.close()
    try:
        import resource
        rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss_bytes=rss*1024 if platform.system()=='Linux' else None
    except ImportError:rss_bytes=None
    print(json.dumps({'status':'PASS','synthetic_rows':a.rows,'unique_schools':schools,'drafts':drafts,'import_seconds':round(import_seconds,3),'generation_seconds':round(duration,3),'process_peak_rss_bytes':rss_bytes,'measurement_platform':platform.system(),'sqlite_bytes':(root/'test.sqlite').stat().st_size,'network_requests':0,'wordpress_writes':0,'scope':'Local synthetic SQLite, not Windows4GB/LocalWP/national555k benchmark'}))
