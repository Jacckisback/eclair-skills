# Contributing · Contribuer · Contribuir · Mitwirken · Contribuire · Contribuir

[English](#english) · [Français](#français) · [Español](#español) · [Deutsch](#deutsch) · [Italiano](#italiano) · [Português](#português)

**Checklist (all languages)**

```bash
python3 scripts/validate_skills.py
python3 scripts/build_skills.py           # after changing scripts/skill_specs_*.py (generated skills, catalog.json)
python3 scripts/build_readmes.py          # after changing catalog.json or scripts/readme_data_*.py
python3 scripts/check_release.py --write  # regenerate SHA256SUMS.json after an intentional change
python3 scripts/check_release.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## English
Open an issue first to discuss a new skill or a contract change. One skill = one folder `skills/eclair-<name>/` with `SKILL.md` (front matter `name` + `description`) and its local `references/`; never merge several skills into one `SKILL.md`. Update `catalog.json`, add the skill’s one-line description in the six languages in `scripts/readme_data_skills.py`, regenerate the READMEs and checksums, and run the checklist. Never claim guaranteed Lighthouse scores, rankings or AI citations: they are measured. Keep guides, examples and experimental prototypes clearly separate. Contributions are licensed under AGPL-3.0-only.

## Français
Ouvrez d’abord une issue pour discuter d’un nouveau skill ou d’un changement de contrat. Un skill = un dossier `skills/eclair-<nom>/` avec `SKILL.md` (en-tête `name` + `description`) et ses `references/` locales ; ne regroupez jamais plusieurs skills dans un seul `SKILL.md`. Mettez à jour `catalog.json`, ajoutez la description en une ligne dans les six langues dans `scripts/readme_data_skills.py`, régénérez les README et les empreintes, puis lancez la liste de contrôle. N’annoncez aucune garantie (Lighthouse, positions Google, citations IA) : cela se mesure. Séparez clairement guides, exemples et prototypes expérimentaux. Les contributions sont publiées sous AGPL-3.0-only.

## Español
Abre primero una issue para hablar de un nuevo skill o de un cambio de contrato. Un skill = una carpeta `skills/eclair-<nombre>/` con `SKILL.md` (cabecera `name` + `description`) y sus `references/` locales; nunca juntes varios skills en un solo `SKILL.md`. Actualiza `catalog.json`, añade la descripción de una línea en los seis idiomas en `scripts/readme_data_skills.py`, regenera los README y las sumas de control y ejecuta la lista de comprobación. No prometas puntuaciones Lighthouse, posiciones ni citas de IA: se miden. Separa claramente guías, ejemplos y prototipos experimentales. Las contribuciones se publican bajo AGPL-3.0-only.

## Deutsch
Eröffne zuerst ein Issue, um einen neuen Skill oder eine Vertragsänderung zu besprechen. Ein Skill = ein Ordner `skills/eclair-<name>/` mit `SKILL.md` (Kopf `name` + `description`) und eigenen `references/`; fasse nie mehrere Skills in einer `SKILL.md` zusammen. Aktualisiere `catalog.json`, ergänze die Einzeilenbeschreibung in allen sechs Sprachen in `scripts/readme_data_skills.py`, erzeuge READMEs und Prüfsummen neu und führe die Checkliste aus. Versprich keine Lighthouse-Werte, Rankings oder KI-Zitate: sie werden gemessen. Trenne Leitfäden, Beispiele und experimentelle Prototypen klar. Beiträge stehen unter AGPL-3.0-only.

## Italiano
Apri prima una issue per discutere una nuova skill o una modifica del contratto. Una skill = una cartella `skills/eclair-<nome>/` con `SKILL.md` (intestazione `name` + `description`) e i suoi `references/` locali; non unire mai più skill in un solo `SKILL.md`. Aggiorna `catalog.json`, aggiungi la descrizione di una riga nelle sei lingue in `scripts/readme_data_skills.py`, rigenera README e checksum ed esegui la checklist. Non promettere punteggi Lighthouse, posizionamenti o citazioni IA: si misurano. Separa chiaramente guide, esempi e prototipi sperimentali. I contributi sono rilasciati sotto AGPL-3.0-only.

## Português
Abra primeiro uma issue para discutir uma nova skill ou uma alteração de contrato. Uma skill = uma pasta `skills/eclair-<nome>/` com `SKILL.md` (cabeçalho `name` + `description`) e as suas `references/` locais; nunca junte várias skills num só `SKILL.md`. Atualize `catalog.json`, adicione a descrição de uma linha nas seis línguas em `scripts/readme_data_skills.py`, regenere os README e as somas de verificação e execute a lista de verificação. Não prometa pontuações Lighthouse, posições ou citações de IA: medem-se. Separe claramente guias, exemplos e protótipos experimentais. As contribuições são publicadas sob AGPL-3.0-only.
