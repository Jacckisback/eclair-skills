---
name: eclair-geo-optimization
description: "Make pages easy to read for search engines and AI assistants (GEO). Use on Éclair CMS 2.x when the user wants to: faciliter lisibilité des pages pour moteurs et assistants ia. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# GEO et agents IA — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **faciliter lisibilité des pages pour moteurs et assistants ia**. Cette fonction est **réalisable aujourd'hui** avec le contrat natif (thème, blocs, routes GET, pages d'administration, tâches). Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Extensions llms.txt et SEO pour les IA. Famille : SEO, GEO et migration.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Contenu vérifiable, provenance, sémantique, llms.txt, Markdown, Schema.org**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Auditer structure, réponses factuelles, sources et cohérence du Markdown; contrôler robots IA sans sur-promesse. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Les SEO/GEO de base sont natifs. Les extensions ne disposent pas encore d’une API universelle pour injecter le JSON-LD; documenter l’écart de contrat plutôt que bricoler le HTML ou des scripts.
7. **Invariant de sécurité :** Ne pas confondre score GEO interne, citabilité et classement garanti. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Tester version Markdown, citations structurées et robots.txt » et le test de refus « Les faits affichés pour robots et humains restent cohérents et à jour ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` ou paquet de thème validé, seulement si un bloc ou un réglage natif ne suffit pas.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Tester version Markdown, citations structurées et robots.txt.
- Les faits affichés pour robots et humains restent cohérents et à jour.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `native-v2-workflow`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
