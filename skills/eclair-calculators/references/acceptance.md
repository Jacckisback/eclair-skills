# Plan de validation — Simulateurs et calculateurs

## Modèle de données
Paramètres, formule, résultat.

## Mise en œuvre attendue
Calculer dans le navigateur avec une formule validée par le client, afficher hypothèses et limites, proposer ensuite la prise de contact.

## Tests à prévoir
1. Nominal : Comparer les résultats à un jeu de cas calculés à la main.
2. Contrôle de refus : Une valeur absurde ou négative affiche un message, pas un résultat faux.
3. Invariant : Le résultat est indicatif et annoncé comme tel ; aucune saisie n'est envoyée au serveur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
