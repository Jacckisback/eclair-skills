# Plan de validation — Tâches planifiées

## Modèle de données
Tâche, fréquence, dernier passage, résultat.

## Mise en œuvre attendue
Déclarer la tâche dans le manifeste (au plus une fois par heure), appeler l'adresse secrète du noyau depuis le planificateur de l'hébergeur, journaliser.

## Tests à prévoir
1. Nominal : Exécuter la tâche deux fois de suite et vérifier un seul effet.
2. Contrôle de refus : Un appel sans le jeton secret ne déclenche rien.
3. Invariant : L'adresse secrète des tâches n'est jamais publiée ; chaque tâche est idempotente.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
