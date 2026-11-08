---
name: eclair-storage
description: Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress.
---

# Éclair Storage — choisir la bonne persistance

## Décision de stockage
1. Pour contenu et réglages Éclair, utiliser `Eclair\Store` et le préfixe `data/ext/<id>/` obtenu via `$ctx['data']`.
2. Vérifier `Store::locked`, écritures atomiques et volumes réellement manipulés ; ne pas inventer de garantie multi-fichiers transactionnelle.
3. Pour commandes/paiements/stocks et progression LMS concurrente : spécifier SQLite ou MySQL **comme dépendance optionnelle du module** avec ses migrations, contraintes, transactions, backup et reprise. Le contrat natif v2 ne fournit pas de PDO générique pour les extensions.
4. Déclarer données personnelles, rétention, suppression et export ; ne pas conserver clés ni jetons dans les sauvegardes.
5. Migrations natives de fonction via manifeste `migrations[]` et méthode `migrate` : additives, versionnées, idempotentes. Une migration de schéma SQL doit avoir un plan séparé, pas être déclenchée sur une page GET.
6. Prévoir sauvegarde cohérente, restauration à froid et test de rollback. Si SQL indisponible sur hébergement mutualisé, annoncer la fonctionnalité indisponible plutôt que retomber sur une persistance non fiable.
7. Tester les collisions, redémarrages, concurrence, doublons, corruption, chmod/symlink, backup et réconciliation.

## Règles
Le stockage natif sans base doit rester possible pour un site simple. Les prototypes SQL v0.5/v0.8 ne sont pas installés ni reconnus par v2. Ne pas promettre exactement-une-fois pour les effets externes.

## Livrables
Schéma, matrice des invariants, protocole de migration/restore, exigences d'hébergement, tests de transaction et d'intégrité.

## V1.0 — Modèle de comptes légers
Le prototype `member-directory` respecte `data/ext/<id>/`, des écritures atomiques et un verrou global. Le stockage en plusieurs fichiers **n'est pas une transaction SQL**. Le quota de 1 000 comptes est une limite de laboratoire : tout projet commercial avec beaucoup de membres doit d'abord disposer du contrat SQL transactionnel.

## Éclair 2.0 — prototype v1.1 (experimental)
Le stockage du démonstrateur utilise encore les fichiers protégés de `Store` et un verrou global. Il est borné à 1000 comptes; aucune promesse d’atomicité multi-fichiers, d’accès à grande échelle ou de tolérance aux pannes transactionnelles. Un backend SQL est un prérequis avant exploitation métier.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
