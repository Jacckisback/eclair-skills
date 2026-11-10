---
name: eclair-moderation
description: "Build removal, reporting and appeal tools. Use on Éclair CMS 2.x when the user wants to: construire outils de retrait, signalement et appel. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Modération et signalements — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **construire outils de retrait, signalement et appel**. Cette fonction **exige des capacités absentes du noyau 2.0** : le skill livre conception, maquette sûre et tests, pas une mise en production. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Outils de modération de bbPress et BuddyPress. Famille : Forum et communauté.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Signalement, motif, élément visé, décision, modérateur, audit**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Prévoir file de traitement, signalements abusifs, seuils/quotas, rollback et motifs; tracer décisions et restreindre pouvoirs par rôle. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Les catégories et listes publiques peuvent être GET; publications, signalements, profils privés et modération exigent une identité et des routes d’écriture sûres, anti-spam et stockage adapté.
7. **Invariant de sécurité :** Aucune suppression définitive automatique par signalement sans contrôle et preuves. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Tester modérateur sans droit global, utilisateur suspendu et appel » et le test de refus « Un modérateur d’une catégorie ne peut pas voir les signalements privés d’une autre ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Dossier de conception, maquette GET sûre si utile, tests bloquants et demande d'évolution du noyau ; **pas de paquet de production**.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Tester modérateur sans droit global, utilisateur suspendu et appel.
- Un modérateur d’une catégorie ne peut pas voir les signalements privés d’une autre.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
