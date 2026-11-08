#!/usr/bin/env python3
"""Release integrity check for Éclair Skills (stdlib only).

Checks that:
- LICENSE contains the GNU AGPL v3.0 text;
- SHA256SUMS.json lists every file of the repository (except itself,
  SIGNATURE.json, the .git directory and ignored caches) with a matching
  SHA-256 digest, and no symbolic link is present;
- catalog.json declares 57 skills in eight families, matching skills/.

Use --write to regenerate SHA256SUMS.json after an intentional change.
This is NOT a security audit and does not qualify any example for production.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMS = 'SHA256SUMS.json'
SIGNATURE = 'SIGNATURE.json'
SKIP_DIRS = {'.git', '__pycache__'}
EXPECTED = {'foundation': 8, 'commerce': 10, 'lms': 7, 'community': 6,
            'business': 8, 'design': 7, 'seo': 5, 'integrations': 6}


def files(root):
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if p.is_file() and not SKIP_DIRS.intersection(rel.parts) \
                and rel.as_posix() not in (SUMS, SIGNATURE) and p.suffix != '.pyc':
            yield rel.as_posix(), p


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true', help='regenerate SHA256SUMS.json')
    args = ap.parse_args()
    current = {rel: digest(p) for rel, p in files(ROOT)}
    if args.write:
        (ROOT / SUMS).write_text(json.dumps(current, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(f'WROTE {SUMS}: {len(current)} files')
        return 0
    errors = []
    for p in ROOT.rglob('*'):
        rel = p.relative_to(ROOT)
        if p.is_symlink() and not SKIP_DIRS.intersection(rel.parts):
            errors.append(f'Symbolic link refused: {rel.as_posix()}')
    lic = (ROOT / 'LICENSE').read_text(encoding='utf-8') if (ROOT / 'LICENSE').is_file() else ''
    if 'GNU AFFERO GENERAL PUBLIC LICENSE' not in lic or 'Version 3, 19 November 2007' not in lic \
            or 'END OF TERMS AND CONDITIONS' not in lic:
        errors.append('LICENSE is not the full GNU AGPL v3.0 text')
    recorded = json.loads((ROOT / SUMS).read_text(encoding='utf-8'))
    for rel in sorted(set(current) - set(recorded)):
        errors.append(f'Not listed in {SUMS}: {rel}')
    for rel in sorted(set(recorded) - set(current)):
        errors.append(f'Listed but missing: {rel}')
    for rel in sorted(set(current) & set(recorded)):
        if current[rel] != recorded[rel]:
            errors.append(f'Digest mismatch: {rel}')
    cat = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    counts = {}
    for s in cat['skills']:
        counts[s['category']] = counts.get(s['category'], 0) + 1
    if counts != EXPECTED:
        errors.append(f'Unexpected family counts: {counts}')
    dirs = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    if dirs != {s['name'] for s in cat['skills']}:
        errors.append('skills/ directories differ from catalog.json')
    if errors:
        print('FAIL:\n- ' + '\n- '.join(errors))
        return 1
    print(f'PASS: release integrity — {len(current)} files hashed, 57 skills in 8 families, AGPL v3.0 LICENSE present')
    return 0


if __name__ == '__main__':
    sys.exit(main())
