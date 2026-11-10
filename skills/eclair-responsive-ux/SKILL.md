---
name: eclair-responsive-ux
description: "Optimise navigation, forms and layouts on mobile. Use on Éclair CMS 2.x when the user wants to: optimiser navigation, formulaires et compositions mobiles. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# UX responsive — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **optimiser navigation, formulaires et compositions mobiles**. Cette fonction est **réalisable aujourd'hui** avec le contrat natif (thème, blocs, routes GET, pages d'administration, tâches). Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Réglages responsive des constructeurs de pages. Famille : Design et UX.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Breakpoints, densité, largeur de texte, menu, formulaires et médias**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Concevoir mobile-first; garder hiérarchie de l’information; tester petits écrans, tailles de cibles et orientations. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Éclair v2 expose des thèmes sous site/themes et des blocs déclaratifs d’extension. Ne modifier ni app/, ni index.php, ni la CSP, ni la génération du cache; valider les thèmes via tools/validate.php.
7. **Invariant de sécurité :** Aucun contenu essentiel caché sur mobile ou dépendant d’animation. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Tester 320px, 375px, tablette et clavier mobile » et le test de refus « Une action primaire reste visible et utilisable sur écran étroit sans scroll horizontal ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` ou paquet de thème validé, seulement si un bloc ou un réglage natif ne suffit pas.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Tester 320px, 375px, tablette et clavier mobile.
- Une action primaire reste visible et utilisable sur écran étroit sans scroll horizontal.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `native-v2-workflow`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
