# Plan de validation — Double authentification

## Modèle de données
Compte, secret TOTP, codes de secours.

## Mise en œuvre attendue
Faire activer la double authentification par chaque personne, ranger les codes de secours, prévoir la perte d'appareil.

## Tests à prévoir
1. Nominal : Activer, se déconnecter, se reconnecter avec le second facteur.
2. Contrôle de refus : Un mot de passe correct sans second facteur ne donne pas accès.
3. Invariant : Les secrets et codes de secours ne sont jamais copiés dans un chat, un e-mail ou un dépôt.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
