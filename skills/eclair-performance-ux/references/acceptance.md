# Plan de validation — Performance UX

## Modèle de données
LCP, CLS, INP, poids d’assets, CSS, JS, cache et polices.

## Mise en œuvre attendue
Mesurer avant/après via tools/measure.php --check, Chrome Lighthouse et réseau lent, optimiser images et scripts.

## Tests à prévoir
1. Nominal : Tester site public sans extension, avec extension et sur mobile.
2. Contrôle de refus : Une amélioration déclarée est accompagnée de mesures reproductibles avant/après.
3. Invariant : Ne pas dégrader le chemin de cache PHP ni désactiver CSP pour gagner en facilité.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
