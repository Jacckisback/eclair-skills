# Plan de validation — Mises à jour et retour arrière

## Modèle de données
Version installée, version annoncée, signature, point de retour.

## Mise en œuvre attendue
Sauvegarder, lire les notes de version, lancer la mise à jour en un clic, vérifier le site, savoir revenir à la version précédente.

## Tests à prévoir
1. Nominal : Mettre à jour une copie du site puis revenir en arrière.
2. Contrôle de refus : Une annonce de mise à jour non signée par le mainteneur est refusée.
3. Invariant : Ne jamais installer une archive dont la signature n'est pas vérifiée par le noyau.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
