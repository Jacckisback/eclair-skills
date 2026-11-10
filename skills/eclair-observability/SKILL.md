---
name: eclair-observability
description: "Monitor health, costs and incidents of modules, with alerts. Use on Éclair CMS 2.x when the user wants to: surveiller santé, coûts et incidents des modules. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Observabilité et alertes — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **surveiller santé, coûts et incidents des modules**. Cette fonction **exige des capacités absentes du noyau 2.0** : le skill livre conception, maquette sûre et tests, pas une mise en production. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Query Monitor, extensions de surveillance. Famille : Intégrations et automatisations.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Logs structurés, erreurs, corrélations, métriques, traces, rétention**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Définir alertes utiles, anonymiser données, surveiller tâches et cache, distinguer incident site et module, fournir runbook. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Les tâches natives existent (minimum 3 600 secondes). Les webhooks entrants et interactions membres requièrent des routes POST qualifiées, une validation de signature et, pour les effets métiers, une outbox idempotente.
7. **Invariant de sécurité :** Aucun mot de passe, jeton, paiement ou PII brute dans les logs; pas de télémétrie cachée. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Tester hausse erreurs 5xx, retard des tâches et disque plein » et le test de refus « Un module désactivé ne continue pas à envoyer de données ni à exécuter de tâches ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Dossier de conception, maquette GET sûre si utile, tests bloquants et demande d'évolution du noyau ; **pas de paquet de production**.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Tester hausse erreurs 5xx, retard des tâches et disque plein.
- Un module désactivé ne continue pas à envoyer de données ni à exécuter de tâches.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
