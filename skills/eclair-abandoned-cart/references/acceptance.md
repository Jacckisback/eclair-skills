# Plan de validation — Relance de panier abandonné

## Modèle de données
Panier, contact, consentement, relance.

## Mise en œuvre attendue
Vérifier la base légale, limiter le nombre de relances, s'appuyer sur les outils du prestataire de paiement quand ils existent.

## Tests à prévoir
1. Nominal : Simuler abandon, relance et désinscription.
2. Contrôle de refus : Un contact désinscrit ne reçoit aucune relance.
3. Invariant : Aucune relance sans consentement ou base légale ; désinscription immédiate.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
