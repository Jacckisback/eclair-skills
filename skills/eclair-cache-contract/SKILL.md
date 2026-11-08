---
name: eclair-cache-contract
description: Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets.
---

# Éclair Cache Contract — garder le cache sûr

## Décision
1. Lire `eclair/index.php`, `Cache.php`, `Extensions::route()` et `docs/EXTENSION-CONTRACT.md` du noyau v2 ciblé.
2. Pour les pages de fonction à contenu public identique pour tous, `routes.public[].cache` peut être `true` après vérification des dépendances de rendu.
3. Pour contenus privés, états utilisateur, paniers, jetons ou prix personnalisés : **pas de cache partagé** (`Cache-Control: private, no-store`), `noindex` pertinent et contrat d'authentification serveur. Ne jamais prétendre qu'un `cache:false` implémente à lui seul l'authentification.
4. Mesurer GET/HEAD et query strings, première génération puis cache HIT, édition des données, activation/désactivation et migrations. Vérifier les routes CMS et l'index `data/ext-public.php`.
5. Ne jamais ajouter de lookup ou de lecture de registre au chemin rapide `index.php` sans un budget mesuré et une justification sécurité.
6. Tester `php tools/measure.php --check` et les budgets dans `tools/budgets.json`, puis comparer à un baseline propre avec la même version PHP et données.
7. Vérifier purge après activation et que les pages publiques non concernées restent cacheables ; tester cookies et en-têtes en situation concurrente.

## Livrables
Matrice URL × méthode × identité × cache, mesures et tests d'isolation.

## V1.0 — Identité et cache
Ne jamais servir une page personnalisée à partir d'un cache partagé. Les routes administrateur existantes sont déjà `private, no-store`; les futures pages publiques membres nécessitent un contrat de route privée avant toute ouverture. Ne jamais supposer que `cache:false` implémente automatiquement des garanties complètes de session/CSRF.

## Éclair 2.0 — prototype v1.1 (experimental)
Les formulaires publics GET utilisent `Security::formField()` et doivent être déclarés `cache:false`. Leurs réponses ne doivent pas atteindre le fast path du noyau. POST est exclu du fast path et forcé no-store. Tester la purge à l’activation du module et vérifier l’absence de cookies/identités dans le HTML de cache partagé.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
