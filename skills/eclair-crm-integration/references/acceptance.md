# Plan de validation — Synchronisation CRM

## Modèle de données
Contact, entreprise, consentement, mapping, clé externe, provenance.

## Implémentation attendue
Mapper champs stricts, différencier mises à jour directionnelles et fusion, fournir réconciliation et export/suppression.

## Tests à prévoir
1. Nominal : Tester fusion, email modifié, conflit, suppression et reprise.
2. Contrôle de refus : Même contact resynchronisé ne crée pas plusieurs doublons dans le CRM.
3. Invariant : Ne pas exporter contacts sans base légale ni scopes minimaux.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
