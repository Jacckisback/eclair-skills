# Plan de validation — Événements et billets

## Modèle de données
Événement, séance, type de place, réservation, billet, scan, remboursement.

## Implémentation attendue
Séparer quotas par séance; émettre billets uniques après paiement confirmé; gérer contrôle d’entrée atomique et transfert.

## Tests à prévoir
1. Nominal : Tester double scan, annulation et dernier billet simultané.
2. Contrôle de refus : Même billet présenté à deux portes => une seule admission acceptée.
3. Invariant : QR code ne contient pas de données personnelles en clair et n’autorise pas plusieurs entrées.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
