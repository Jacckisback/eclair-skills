---
name: eclair-digital-downloads
description: "Design the sale of files with secure delivery. Use on Éclair CMS 2.x when the user wants to: concevoir la vente de fichiers avec livraison sécurisée. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Produits numériques — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **concevoir la vente de fichiers avec livraison sécurisée**. Cette fonction **exige des capacités absentes du noyau 2.0** : le skill livre conception, maquette sûre et tests, pas une mise en production. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Easy Digital Downloads. Famille : Commerce Pro.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Produit numérique, achat, lien de livraison temporaire**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Faire livrer le fichier par le prestataire ou par lien signé à durée limitée ; ne jamais placer le fichier à une adresse publique. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Cette fonction demande des écritures de visiteurs, des comptes publics, des transactions ou des événements signés que `eclair-extension/1` ne fournit pas en 2.0. Livrer la conception, une maquette GET sûre et des tests bloquants ; ne jamais annoncer une mise en production.
7. **Invariant de sécurité :** Aucun fichier payant n'est accessible sans achat vérifié. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Simuler achat, livraison et expiration du lien » et le test de refus « Un lien expiré ou partagé ne donne plus accès au fichier ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Dossier de conception, maquette GET sûre si utile, tests bloquants et demande d'évolution du noyau ; **pas de paquet de production**.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Simuler achat, livraison et expiration du lien.
- Un lien expiré ou partagé ne donne plus accès au fichier.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
