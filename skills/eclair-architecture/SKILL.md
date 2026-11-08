---
name: eclair-architecture
description: Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC.
---

# Éclair Architecture — préserver le noyau v2

## Objectif
Concevoir la solution demandée **sans recopier un système d’extensions** et sans surcharger la route de cache. Commencer par `references/core-map.md` et le code du checkout courant.

## Déroulé opérationnel
1. Relever le commit, la version `ECLAIR_VERSION`, PHP et les capacités disponibles par `/admin/api/capabilities` si l'accès est autorisé.
2. Classer l'objectif : contenu/réglage natif, thème de site, fonction `eclair-extension/1`, service externe, ou manque du contrat public nécessitant une RFC.
3. Chercher d'abord `Extensions`, `Themes`, `Packages`, `Migrations`, `Store`, `Cache`, `Site`, `Seo`, `Security`, `Mcp` et les docs `docs/ARCHITECTURE-2.md`/`docs/STATUS-2.md`.
4. Décrire les frontières : code sous `site/extensions/` ou `site/themes/`, données via `Store` et `$ctx['data']`, médias sous `media/`, aucun remplacement de `app/`.
5. Distinguer strictement le contrat natif (`eclair-extension/1`) des anciennes expérimentations v0.8 (routes/permissions/SQL/outbox), incompatibles avec v2 sans portage.
6. Produire une décision d'architecture explicite : alternatives, limites de l'API, risques, rollback, test de compatibilité et indicateurs de performance.
7. Faire relire puis valider avec `php tests/run.php`, `php tools/measure.php --check` et les tests pertinents de `tests/extensions.php`.

## Non négociables
Préserver SEO/GEO, balisage canonique, protections CSRF/CSP, gestion de l'auth et cache chaud. Une extension ne s'active jamais elle-même. Ne prétendre ni gérer un checkout transactionnel, ni les comptes élèves, tant que ces contrats ne sont pas implémentés et testés.

## Livrables
ADR et cartographie avant/après, décision « native / extension / core RFC », contraintes, tests et plan de retour arrière. Le modèle `assets/architecture-decision.md` peut servir de point de départ.

## V1.0 — Extensions membres
La fonction native `examples/extensions/member-directory` illustre les comptes publics séparés : aucun nouveau rôle dans `Eclair\Users`. Un noyau 2.0 reçoit les extensions via `site/extensions/<id>`; aucune écriture dans `app/`.

## Éclair 2.0 — prototype v1.1 (experimental)
Éclair 2.0.0 possède désormais un contrat expérimental de POST public uniquement si le patch v1.1 est appliqué sur une branche de développement. Le noyau officiel ne fournit **pas** ce contrat. Aucune modification directe du noyau depuis un skill; préparation d’une RFC et tests préalables.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
