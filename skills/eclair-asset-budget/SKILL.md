---
name: eclair-asset-budget
description: "Keep a weight budget for CSS, JavaScript and images. Use on Éclair CMS 2.x when the user wants to: tenir un budget de poids pour CSS, JavaScript et images. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Budget de poids — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **tenir un budget de poids pour CSS, JavaScript et images**. Cette fonction est **réalisable aujourd'hui** avec le contrat natif (thème, blocs, routes GET, pages d'administration, tâches). Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Autoptimize, Asset CleanUp. Famille : Performance.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Budget par type de ressource, mesure, écart**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Fixer des budgets par page type, mesurer avec l'outil du noyau, refuser tout ajout qui les dépasse sans justification. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Réalisable avec `eclair-extension/1` et le contrat de thème : routes GET publiques cacheables, pages d'administration protégées, blocs et réglages déclaratifs, tâches planifiées, actifs. Vérifier d'abord qu'un bloc ou un réglage natif ne suffit pas.
7. **Invariant de sécurité :** Aucune dépendance tierce chargée pour une fonction décorative. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Lancer la mesure des budgets sur le site et sur le paquet produit » et le test de refus « Un paquet qui dépasse le budget n'est pas livré tel quel ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` ou paquet de thème validé, seulement si un bloc ou un réglage natif ne suffit pas.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Lancer la mesure des budgets sur le site et sur le paquet produit.
- Un paquet qui dépasse le budget n'est pas livré tel quel.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `native-v2-workflow`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
