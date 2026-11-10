# Plan de validation — Synchronisation CRM

## Modèle de données
Contact, entreprise, consentement, mapping, clé externe, provenance.

## Mise en œuvre attendue
Mapper champs stricts, différencier mises à jour directionnelles et fusion, fournir réconciliation et export/suppression.

## Tests à prévoir
1. Nominal : Tester fusion, email modifié, conflit, suppression et reprise.
2. Contrôle de refus : Même contact resynchronisé ne crée pas plusieurs doublons dans le CRM.
3. Invariant : Ne pas exporter contacts sans base légale ni scopes minimaux.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
