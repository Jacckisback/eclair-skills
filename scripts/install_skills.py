#!/usr/bin/env python3
"""Install Éclair Agent Skills by family or name into .agents/skills (Codex convention)."""
import argparse
import re
import shutil
from pathlib import Path
from validate_skills import catalog,validate
ROOT=Path(__file__).resolve().parents[1]

def choose(root, categories=None, names=None):
    entries=catalog(root)
    family=set(categories or [])
    requested=set(names or [])
    valid_families={x['category'] for x in entries}
    valid_names={x['name'] for x in entries}
    unknown_f=family-valid_families
    unknown_n=requested-valid_names
    if unknown_f or unknown_n:
        raise ValueError(f'Unknown selections: categories={sorted(unknown_f)}, skills={sorted(unknown_n)}')
    if not family and not requested:
        return [x['name'] for x in entries]
    return [x['name'] for x in entries if x['category'] in family or x['name'] in requested]

def source_dir(root:Path,lang='fr'):
    lang=(lang or 'fr').lower()
    if lang=='fr':return root/'skills'
    d=root/'translations'/lang
    if not re.fullmatch(r'[a-z]{2}',lang) or not d.is_dir():
        available=['fr']+sorted(p.name for p in (root/'translations').iterdir() if p.is_dir()) if (root/'translations').is_dir() else ['fr']
        raise ValueError(f'Unknown language {lang!r}; available: '+', '.join(available))
    return d

def install(root:Path,project:Path,force=False,categories=None,names=None,lang='fr'):
    root=root.resolve();project=project.resolve()
    if not project.is_dir():raise ValueError('Project directory does not exist')
    if project==root or project in root.parents:raise ValueError('Destination inside source library not allowed')
    issues=validate(root)
    if issues:raise ValueError('Invalid library: '+'; '.join(issues))
    selected=choose(root,categories,names)
    src=source_dir(root,lang)
    target=project/'.agents'/'skills'
    # Existing symlink traversal is rejected for all path components.
    for component in [project/'.agents',target]:
        if component.is_symlink():raise ValueError(f'Symlink destination refused: {component}')
    if target.exists() and target.resolve()!=target.absolute():
        raise ValueError('Resolved target differs from requested target')
    # Preflight prevents partial installs due to collisions.
    collided=[n for n in selected if (target/n).exists() or (target/n).is_symlink()]
    if collided and not force:raise FileExistsError('Existing skill(s); use --force: '+', '.join(collided))
    for n in selected:
        if (target/n).is_symlink():raise ValueError(f'Symlink skill destination refused: {n}')
    target.mkdir(parents=True,exist_ok=True)
    for n in selected:
        dst=target/n
        if dst.exists():shutil.rmtree(dst)
        shutil.copytree(src/n,dst)
    return target

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=ROOT)
    p.add_argument('--project',type=Path)
    p.add_argument('--category',action='append',default=[],help='Select a skill family, repeatable')
    p.add_argument('--skill',action='append',default=[],help='Select specific skill, repeatable')
    p.add_argument('--all',action='store_true',help='Install every skill of the catalogue')
    p.add_argument('--list',action='store_true',help='List skills and groups without installing')
    p.add_argument('--lang',default='fr',help='Language of the installed skills: fr (default), en, es, de, it, pt')
    p.add_argument('--force',action='store_true',help='Replace selected installed skills')
    a=p.parse_args()
    if a.all and (a.category or a.skill):p.error('--all cannot be combined with filters')
    try:
        if a.list:
            for row in catalog(a.root.resolve()):print(row['category'],row['name'])
            return
        if a.project is None:p.error('--project is required except with --list')
        selected=choose(a.root.resolve(),a.category,a.skill)
        output=install(a.root,a.project,a.force,a.category,a.skill,a.lang)
        print(f'Installed {len(selected)} skills ({a.lang}) to {output}')
    except (OSError,ValueError) as exc:p.error(str(exc))
if __name__=='__main__':main()
