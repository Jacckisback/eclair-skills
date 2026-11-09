# Plan de validation — Mode sombre

## Modèle de données
Jeux de couleurs clair et sombre, préférence du visiteur.

## Mise en œuvre attendue
Définir les variables de couleur du thème pour prefers-color-scheme, vérifier contrastes, images et logos.

## Tests à prévoir
1. Nominal : Contrôler les contrastes des deux modes sur les pages types.
2. Contrôle de refus : Un logo sombre ne devient pas invisible en mode sombre.
3. Invariant : Aucun cookie n'est nécessaire pour respecter la préférence système.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
