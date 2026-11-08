#!/usr/bin/env python3
"""Read-only drift audit for the *native* Éclair CMS 2.0 extension contract.
Text markers are diagnostic only, never a substitute for PHP tests or official validator.
"""
from pathlib import Path
import argparse,re,sys
REQUIRED={
    'eclair/index.php':['ECLAIR_VERSION'],
    'eclair/app/lib/Extensions.php':['class Extensions',"eclair-extension/1", 'function validate', 'function activate'],
    'eclair/app/lib/AdminExtensions.php':['class AdminExtensions'],
    'eclair/app/lib/Store.php':['class Store','function locked'],
    'eclair/app/lib/Cache.php':['class Cache','function purge'],
    'eclair/app/lib/Auth.php':['class Auth','function can'],
    'tools/validate.php':['Extensions::validate'],
    'docs/EXTENSION-CONTRACT.md':['eclair-extension/1'],
    'docs/SKILLS-GUIDE.md':['site/extensions/'],
    'docs/schemas/extension.schema.json':['eclair-extension/1'],
    'tests/extensions.php':['Extensions::validate'],
    'tests/run.php':['--unit'],
    'tools/measure.php':['--check'],
}
def check_core(root:Path):
    issues=[]
    if not root.is_dir():return ['Repository checkout not found']
    for file, markers in REQUIRED.items():
        p=root/file
        if not p.is_file():issues.append(f'Missing: {file}');continue
        s=p.read_text('utf-8',errors='replace')
        for marker in markers:
            if marker not in s:issues.append(f'Contract drift: {file} lacks {marker}')
    idx=root/'eclair/index.php'
    if idx.exists():
        m=re.search(r"define\('ECLAIR_VERSION',\s*'([^']+)'\)",idx.read_text('utf-8',errors='replace'))
        if m is None or not m[1].startswith('2.'):
            issues.append('Not an audited Éclair 2.x checkout. Re-audit before using skills.')
    return issues
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--core',required=True,type=Path)
    a=parser.parse_args();errors=check_core(a.core)
    for e in errors:print('DRIFT:',e)
    if errors:sys.exit(1)
    print('PASS: Éclair 2.x native contract markers found (not a security or runtime certification)')
