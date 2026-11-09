# Plan de validation — Assistance et tickets

## Modèle de données
Ticket, demandeur, statut, échanges, priorité.

## Mise en œuvre attendue
Commencer par formulaire de contact et boîte de réception ; concevoir statuts, délais et espace de suivi pour plus tard.

## Tests à prévoir
1. Nominal : Dérouler une demande de l'ouverture à la clôture.
2. Contrôle de refus : Un ticket ne peut pas être lu en devinant son numéro.
3. Invariant : Un demandeur ne voit que ses propres tickets.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
