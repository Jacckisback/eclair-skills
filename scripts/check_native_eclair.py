#!/usr/bin/env python3
"""Run authoritative Éclair 2.0 gates against a developer's patched checkout.

Read-only to source (the official test/build tooling may create test/dist artifacts).
Never writes a patch, changes a branch, publishes code or calls network APIs.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkout', required=True, type=Path, help='local Éclair 2.0 repository root')
    p.add_argument('--skip-full', action='store_true', help='only validate native manifest and PHP syntax, no official suite')
    p.add_argument('--report', type=Path, help='write gate results as JSON (no secrets)')
    a = p.parse_args()
    root = a.checkout.resolve()
    results = []
    def gate(name, passed, detail=''):
        results.append({'gate': name, 'passed': bool(passed), 'detail': detail[:1000]})
        print(('PASS' if passed else 'FAIL') + ': ' + name + (f' — {detail[:160]}' if detail else ''))
        return bool(passed)
    idx = root/'eclair/index.php'
    ex = root/'eclair/app/lib/Extensions.php'
    schema = root/'docs/schemas/extension.schema.json'
    if not all(x.is_file() for x in [idx, ex, schema, root/'tools/validate.php', root/'tests/run.php']):
        gate('Official repository shape', False, 'Missing required Éclair 2.0 sources')
    else:
        version = re.search(r"define\('ECLAIR_VERSION', '([^']+)'\)", idx.read_text())
        gate('Supported core version', bool(version and version.group(1)=='2.0.0'), version.group(1) if version else 'missing')
        content = ex.read_text()
        contract = json.loads(schema.read_text())
        public = contract['properties']['routes']['properties']['public']['items']['properties']['method']['enum']
        gate('Experimental public POST handler enabled', 'Security::checkFormToken()' in content
             and "['GET', 'POST']" in content and 'Http::redirect(path_to($to), 303)' in content
             and '[200, 400, 401, 403, 409, 422, 429, 500, 503]' in content
             and 'ECLAIR_MEMBER_TRUSTED_PROXY_IP' in content and 'POST' in public,
             'POST must be allowed by patched code and schema with explicit trusted-proxy guard')
        if all(i['passed'] for i in results):
            ext = ROOT/'examples/extensions/member-directory'
            if not gate('Official extension validator', *validator(root, ext)):
                pass
            else:
                for rel in ['extension.php','lib/MemberAccounts.php','lib/MemberEnroll.php','lib/MemberPublic.php','lib/MemberTransport.php']:
                    proc = subprocess.run(['php','-l',str(ext/rel)],capture_output=True,text=True)
                    gate('PHP syntax '+rel, proc.returncode==0, (proc.stdout+proc.stderr).strip())
                if not a.skip_full:
                    for label, argv in [('Official CMS PHP suite',['php','tests/run.php']),
                                         ('Official performance budgets',['php','tools/measure.php','--check'])]:
                        proc = subprocess.run(argv,cwd=root,text=True,stdout=subprocess.PIPE,
                                              stderr=subprocess.STDOUT,timeout=900)
                        gate(label, proc.returncode==0, proc.stdout[-950:].strip())
                else:
                    gate('Official CMS PHP suite',False,'SKIPPED by --skip-full; not qualified')
                    gate('Official performance budgets',False,'SKIPPED by --skip-full; not qualified')
    if a.report:
        a.report.parent.mkdir(parents=True,exist_ok=True)
        a.report.write_text(json.dumps({'scope':'local experimental Éclair 2.0 only', 'results':results},indent=2,ensure_ascii=False)+'\n')
    return 0 if results and all(x['passed'] for x in results) else 1

def validator(root, ext):
    proc = subprocess.run(['php','tools/validate.php',str(ext),'--json'],cwd=root,text=True,
                          stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=120)
    try:
        obj = json.loads(proc.stdout)
        return proc.returncode==0 and obj.get('valid') is True, json.dumps(obj,ensure_ascii=False)[:950]
    except ValueError:
        return False,proc.stdout[-950:].strip()

if __name__=='__main__':
    try: sys.exit(main())
    except (OSError, subprocess.TimeoutExpired, ValueError, KeyError) as exc:
        print('FAIL: native gates could not run: '+str(exc),file=sys.stderr)
        sys.exit(2)
