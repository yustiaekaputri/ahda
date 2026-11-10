"""Actual PHP bridge with a WP facade, not a real WordPress/LocalWP integration."""
import json
import os
from pathlib import Path
import subprocess
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
PHP=os.environ.get('PHP_BIN') or shutil.which('php')
@unittest.skipUnless(PHP and Path(PHP).is_file(), 'PHP not available; set PHP_BIN for bridge facade tests')
class PreviewTests(unittest.TestCase):
    def run_preview(self, old='', code='20515441', host='http://ahda.local/', duplicate=False, draftname='SMKN 1 BANDUNG'):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);draft={'npsn':code,'identity':{'name':draftname},'article_text':'Draf sekolah dengan fakta terbatas.','status':'pending_review','wordpress_apply_enabled':False}
            (p/'draft.json').write_text(json.dumps(draft))
            config=json.dumps({'old':old,'host':host,'duplicate':duplicate})
            stub='''<?php
            define('WP_CLI',true);define('ARRAY_A','ARRAY_A');define('AHDA_DIRECTORY_VERSION','0.8.9');
            class WP_CLI {static function line($text){echo $text;} static function error($message){fwrite(STDERR,$message);exit(3);}}
            function current_user_can($cap){return $cap==='manage_options';}
            function home_url($path){global $cfg;return $cfg['host'];}
            class FakeDB {public $prefix='x_',$last_error='';
              function prepare($query,...$args){return $query;}
              function get_results($query,$kind){global $cfg;
                if(strpos($query,'SELECT id,npsn,name,visibility')===0){$r=['id'=>'196744','npsn'=>'20515441','name'=>'SMKN 1 BANDUNG','visibility'=>'publish'];return $cfg['duplicate']?[$r,$r]:[$r];}
                if(strpos($query,'SELECT meta_key,LEFT')===0){return $cfg['old']===''?[]:[['meta_key'=>'profile_description','meta_value'=>$cfg['old'],'value_bytes'=>strlen($cfg['old']),'verification_status'=>'verified']];}
                throw new Exception('Unexpected SQL');}
              function query($query){throw new Exception('Unexpected write');}
              function insert(...$args){throw new Exception('Unexpected insert');}}
            $cfg=json_decode(CONFIG,true);$wpdb=new FakeDB;$args=[DRAFT];include BRIDGE;
            '''.replace('CONFIG',repr(config)).replace('DRAFT',repr(str(p/'draft.json'))).replace('BRIDGE',repr(str(ROOT/'wordpress-preview.php')))
            (p/'stub.php').write_text(stub)
            return subprocess.run([PHP,'-n',str(p/'stub.php')],capture_output=True,text=True)
    def test_empty_existing_profile_is_review_only(self):
        x=self.run_preview();self.assertEqual(x.returncode,0,x.stderr);r=json.loads(x.stdout)
        self.assertEqual(r['school_id'],196744);self.assertFalse(r['apply_supported']);self.assertEqual(r['database_writes'],0)
        self.assertEqual(r['decision'],'NEEDS_ADMIN_SOURCE_AND_CONTENT_REVIEW')
    def test_existing_description_preserved(self):
        x=self.run_preview(old='Existing description');self.assertEqual(x.returncode,0,x.stderr)
        self.assertEqual(json.loads(x.stdout)['decision'],'PRESERVE_EXISTING_DESCRIPTION')
    def test_production_is_rejected_before_queries(self):
        x=self.run_preview(host='https://ahda.sch.id/');self.assertEqual(x.returncode,3);self.assertIn('LOCAL_ADMIN',x.stderr)
    def test_npsn_sql_injection_rejected(self):
        self.assertEqual(self.run_preview(code="1' OR '1").returncode,3)
    def test_duplicate_existing_npsn_rejected(self):
        self.assertEqual(self.run_preview(duplicate=True).returncode,3)
    def test_identity_name_difference_blocks_without_name_join(self):
        x=self.run_preview(draftname='Different School');self.assertEqual(x.returncode,0,x.stderr)
        self.assertEqual(json.loads(x.stdout)['decision'],'BLOCKED_IDENTITY_OR_VISIBILITY')

if __name__=='__main__':unittest.main()
