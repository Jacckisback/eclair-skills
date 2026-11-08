#!/usr/bin/env python3
"""Validate the 57-skill Agent Skills catalog structurally, using Python stdlib.
This is NOT a semantic audit or official Éclair validator.
"""
import argparse
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def catalog(root: Path):
    c=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
    return c['skills']

def validate(root: Path):
    errors=[]
    skill_dir=root/'skills'
    expected={s['name'] for s in catalog(root)}
    existing={p.name for p in skill_dir.iterdir() if p.is_dir()} if skill_dir.is_dir() else set()
    if len(expected)!=len(catalog(root)):
        errors.append('Duplicate skill names in catalog')
    if len(expected)!=57:
        errors.append(f'Wrong skill count: {len(expected)} (expected 57)')
    for unexpected in sorted(existing-expected): errors.append(f'Unexpected skill directory: {unexpected}')
    for n in sorted(expected):
        file=skill_dir/n/'SKILL.md'
        if not file.is_file(): errors.append(f'Missing: {file}');continue
        text=file.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            errors.append(f'Missing YAML frontmatter: {n}');continue
        fm,body=text[4:].split('\n---\n',1)
        values={}
        for line in fm.splitlines():
            if ':' in line:
                k,v=line.split(':',1);values[k.strip()]=v.strip().strip('"\'')
        if values.get('name')!=n: errors.append(f'Frontmatter name mismatch: {n}')
        desc=values.get('description','')
        if not 30<=len(desc)<=1024: errors.append(f'Invalid description: {n}')
        if not re.fullmatch(r'[a-z0-9-]{1,64}',n):errors.append(f'Invalid name: {n}')
        if len(body.strip())<450:errors.append(f'Skill body too short: {n}')
        if not (file.parent/'references/core-map.md').is_file():errors.append(f'Missing core map: {n}')
        for rel in re.findall(r'`((?:assets|references)/[^`]+)`',body):
            if not (file.parent/rel).is_file():errors.append(f'Broken reference: {n}: {rel}')
    return errors

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=ROOT)
    a=ap.parse_args();errors=validate(a.root.resolve())
    if errors:
        for error in errors:print('ERROR:',error)
        raise SystemExit(1)
    print(f'PASS: {len(catalog(a.root.resolve()))} Agent Skills have valid structural packaging')
if __name__=='__main__':main()
