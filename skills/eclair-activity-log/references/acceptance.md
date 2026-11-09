# Plan de validation — Journal d'activité

## Modèle de données
Événement, compte, date, action.

## Mise en œuvre attendue
Consulter le journal de la page Sécurité, repérer connexions et changements sensibles, fixer une routine de contrôle.

## Tests à prévoir
1. Nominal : Provoquer une action sensible et la retrouver dans le journal.
2. Contrôle de refus : Un compte sans droit Sécurité n'accède pas au journal.
3. Invariant : Le journal n'est lisible que par les comptes ayant le droit Sécurité.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
