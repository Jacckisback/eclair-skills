# Plan de validation — Retours et remboursements

## Modèle de données
Demande de retour, motif, état, remboursement.

## Mise en œuvre attendue
Publier la politique de retour native sur les fiches, traiter les demandes par le formulaire de contact, rembourser chez le prestataire ; concevoir le suivi structuré.

## Tests à prévoir
1. Nominal : Dérouler une demande de retour de la réception au remboursement.
2. Contrôle de refus : Une demande hors délai reçoit une réponse motivée, pas un remboursement automatique.
3. Invariant : Un remboursement n'est déclenché que par une personne habilitée, chez le prestataire.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
