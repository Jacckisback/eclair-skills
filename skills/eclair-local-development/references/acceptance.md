# Plan de validation — Développement local

## Modèle de données
Version de PHP, serveur web, copie du site, données de test.

## Mise en œuvre attendue
Installer la même version de PHP et les mêmes règles de serveur, restaurer une sauvegarde anonymisée, lancer les tests.

## Tests à prévoir
1. Nominal : Démarrer le site local et faire passer la suite de tests.
2. Contrôle de refus : Une copie locale n'envoie aucun e-mail réel.
3. Invariant : Les données réelles de clients ne sont pas copiées en local sans anonymisation.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
