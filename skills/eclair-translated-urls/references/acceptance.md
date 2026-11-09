# Plan de validation — Adresses traduites

## Modèle de données
Adresse par langue, redirections, canonical, hreflang.

## Mise en œuvre attendue
Fixer une convention d'adresses par langue, traduire les slugs avant publication, vérifier canonical et hreflang produits par le noyau.

## Tests à prévoir
1. Nominal : Vérifier canonical et hreflang de chaque version.
2. Contrôle de refus : Deux langues ne partagent jamais la même adresse.
3. Invariant : Aucune adresse publiée n'est changée sans redirection.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
