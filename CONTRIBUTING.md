# Contribuer / Contributing

**FR —** Merci de votre intérêt pour Éclair Skills.

1. Ouvrez d'abord une issue pour discuter d'un nouveau skill ou d'un changement de contrat.
2. Un skill = un dossier `skills/eclair-<nom>/` avec `SKILL.md` (front matter `name` + `description`) et ses `references/` locales. Ne regroupez pas plusieurs skills dans un seul `SKILL.md`.
3. Mettez à jour `catalog.json`, puis régénérez les empreintes : `python3 scripts/check_release.py --write`.
4. Avant la PR, lancez :
   ```bash
   python3 scripts/validate_skills.py
   python3 scripts/check_release.py
   python3 -m unittest discover -s tests -p 'test_*.py' -v
   ```
5. N'annoncez aucune garantie (Lighthouse 100, positions Google, citations IA) : ce sont des mesures. Distinguez clairement guides, exemples et prototypes expérimentaux.
6. Toute contribution est publiée sous AGPL-3.0-only.

**EN —** Open an issue first. One skill per folder (`SKILL.md` + `references/`). Update `catalog.json`, regenerate `SHA256SUMS.json` with `python3 scripts/check_release.py --write`, and run the checks above before opening a pull request. Contributions are licensed under AGPL-3.0-only. Never claim guaranteed scores, rankings or AI citations.
