# Plan de validation — Glossaire

## Modèle de données
Terme, définition, termes liés.

## Mise en œuvre attendue
Rédiger une définition claire par terme, classer par ordre alphabétique, relier les termes aux contenus qui les emploient.

## Tests à prévoir
1. Nominal : Naviguer par lettre et suivre les liens entre termes.
2. Contrôle de refus : Un terme sans définition validée n'est pas publié.
3. Invariant : Aucune définition copiée d'une source protégée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
