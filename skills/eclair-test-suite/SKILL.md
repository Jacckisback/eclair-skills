---
name: eclair-test-suite
description: Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations.
---

# Éclair Test Suite — une preuve avant publication

## Ordre de vérification
1. Relever le commit et le `ECLAIR_VERSION` ; exiger le contrat v2 officiel. Sans checkout complet, limiter l'affirmation aux tests réellement exécutables.
2. `php -l` de chaque PHP produit puis `php tools/validate.php site/extensions/<id> --json` avec le noyau correspondant.
3. `php tests/run.php --unit`, puis `php tests/run.php` (HTTP, auth, routes, cache, sauvegardes, extensions, thèmes, migration WordPress).
4. `php tools/measure.php --check` ; comparer le cache chaud et le budget de mémoire/temps au noyau non modifié.
5. Tester installation inactive, activation, migration idempotente, update, conflit route, désactivation, conservation des données, suppression de code et éventuel purge manuel.
6. Si comptes membres/SQL : exiger des tests PHP/PDO réels, multi-processus, autorisations par objet, webhooks signé et restauration depuis sauvegarde. `pdo_sqlite` absent = test bloqué, pas passé.
7. CI recommandée : matrice PHP 8.1 à 8.5, `tests.yml` officiel, archive construite et serveurs Apache/Nginx ; ajouter des jobs spécifiques à la fonctionnalité.
8. Produire une table tests exécutés / échoués / bloqués. Ne jamais rapporter « compatible production » depuis une fixture isolée.

## Livrables
Scripts et fixtures, rapport d'exécution, couverture des cas adverses, budgets et stratégie de rollback.

## V1.0 — Vérifications supplémentaires
Exécuter `php tests/member-directory.php`, `python3 -m unittest discover -s tests -v`, et `python3 scripts/verify_sample.py`. Sur un checkout Éclair 2.0 complet, exécuter **impérativement** `php tools/validate.php examples/extensions/member-directory --json` puis les tests PHP/HTTP du CMS complet et le budget `tools/measure.php --check` avant toute proposition de fusion.

## Éclair 2.0 — prototype v1.1 (experimental)
Tester `php tests/member-directory.php` + `php tests/member-public.php` et les tests Python. Sur un vrai clone Éclair 2.0.0, appliquer le patch à une feature branch propre, faire `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check`, et des essais HTTP/TLS. Aucune fusion sans ces critères.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
