# Plan de validation — Comptes clients

## Modèle de données
Client, identifiants, commandes, adresses.

## Mise en œuvre attendue
Définir inscription, connexion, récupération et suppression de compte ; séparer strictement comptes clients et comptes d'administration.

## Tests à prévoir
1. Nominal : Simuler inscription, connexion, consultation et suppression du compte.
2. Contrôle de refus : Un client ne peut pas lire la commande d'un autre en changeant un identifiant.
3. Invariant : Un client ne voit que ses propres données ; jamais de cache partagé sur l'espace client.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
