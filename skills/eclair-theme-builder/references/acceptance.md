# Plan de validation — Création de thème

## Modèle de données
theme.json, styles, assets, templates déclarés, licence et provenance.

## Mise en œuvre attendue
Partir du thème exemple officiel, employer variables et gabarits supportés, tester preview puis ZIP, vérifier compatibilité version.

## Tests à prévoir
1. Nominal : Tester validateur thème, activation, prévisualisation et retour arrière.
2. Contrôle de refus : Un template défectueux ne rend pas le site inaccessible grâce au repli prévu.
3. Invariant : Ne jamais refaire SEO head et canonical ni toucher aux fichiers noyau.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
