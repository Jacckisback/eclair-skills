# Portes de qualité (Éclair 2.0.0)

- **Gate 0** Vérifier checkout/commit/version + `/admin/api/capabilities` si la session et le droit `settings` sont disponibles.
- **Gate 1** Paquet sous `site/extensions/<id>/`, schéma `eclair-extension/1`, fichiers listés par SHA-256, aucun code noyau modifié.
- **Gate 2** `php tools/validate.php <path> --json` officiel = `valid: true`.
- **Gate 3** `php tests/run.php` complet (unitaires et HTTP), y compris tests d'extensions.
- **Gate 4** `php tools/measure.php --check` sur l'archive et le noyau modifiés selon le cas.
- **Gate 5** tests sécurité négatifs, permissions par objet, isolation des cache privées, sauvegarde restauration et compatibilité PHP.
- **Gate 6** revue humaine, activation depuis l'administration et rollback testé. Aucun MCP ne peut installer du PHP en contournant les droits.

Sans checkout officiel local : linter PHP, validation statique du manifeste et test d'installation des skills **ne valent pas** Gates 2–5.

## Portail membre expérimental v1.1
- [x] Tests PHP isolés du module public et des comptes précédents.
- [x] Tests Python de structure, d’intégrité et du garde-fou de patch sur dépôt Git synthétique.
- [ ] Valider l'extension avec `php tools/validate.php` dans un checkout officiel Éclair 2.0.0 patché.
- [ ] Exécuter `php tests/run.php` et `php tools/measure.php --check` sur les sources et l'archive de distribution.
- [ ] Exercices HTTP/TLS sur vrais Apache/Nginx et navigateurs, reverse proxy compris.
- [ ] Test d'envoi d'email, récupération du mot de passe, inscription autonome et stockage SQL transactionnel.
- [ ] Audit de sécurité de la surface d'authentification.
Aucune publication ni activation en production avant la levée des points bloquants.

## Extension publique v1.2

- [x] Tests PHP isolés d'inscription, vérification, reset et rejet SMTP.
- [x] Contrôles de sécurité du patch sur des dépôts Git **synthétiques**.
- [ ] Exécuter `scripts/check_native_eclair.py --checkout <repo>` dans un checkout réel et patché (Gate native indispensable).
- [ ] Auditer emails réels, TLS Apache/Nginx, non-énumération temporelle, reprise pending et confidentialité des jetons.
- [ ] Vérifier PHP 8.1–8.5 et les budgets performance avant merge.
