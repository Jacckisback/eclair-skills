# Plan de validation — Événements et billets

## Modèle de données
Événement, séance, type de place, réservation, billet, scan, remboursement.

## Mise en œuvre attendue
Séparer quotas par séance; émettre billets uniques après paiement confirmé; gérer contrôle d’entrée atomique et transfert.

## Tests à prévoir
1. Nominal : Tester double scan, annulation et dernier billet simultané.
2. Contrôle de refus : Même billet présenté à deux portes => une seule admission acceptée.
3. Invariant : QR code ne contient pas de données personnelles en clair et n’autorise pas plusieurs entrées.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
