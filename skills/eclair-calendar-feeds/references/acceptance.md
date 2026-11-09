# Plan de validation — Flux de calendrier

## Modèle de données
Événement, date, fuseau, lieu, flux iCalendar.

## Mise en œuvre attendue
Générer un flux iCalendar public en GET à partir des événements publiés, avec fuseaux explicites.

## Tests à prévoir
1. Nominal : S'abonner au flux depuis deux applications de calendrier.
2. Contrôle de refus : Un événement annulé est marqué annulé dans le flux.
3. Invariant : Le flux ne contient que des événements publics, sans participants.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
