# Plan de validation — Abonnements payants

## Modèle de données
Offre, période, abonné, échéance, statut.

## Mise en œuvre attendue
Laisser le prestataire gérer prélèvements et espace client ; concevoir la synchronisation des droits par événements signés.

## Tests à prévoir
1. Nominal : Simuler souscription, renouvellement, échec et résiliation.
2. Contrôle de refus : Un paiement échoué ne prolonge aucun accès.
3. Invariant : Un droit d'accès n'est ouvert que sur un événement de paiement authentifié.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
