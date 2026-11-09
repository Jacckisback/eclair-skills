# Plan de validation — Préproduction et mise en ligne

## Modèle de données
Copie de test, différences, liste de contrôle de mise en ligne.

## Mise en œuvre attendue
Restaurer une sauvegarde sur un sous-domaine protégé et non indexable, y valider thème et fonctions, puis reproduire en production.

## Tests à prévoir
1. Nominal : Dérouler un changement de thème de la copie à la production.
2. Contrôle de refus : La copie de test n'est ni indexée ni accessible sans authentification.
3. Invariant : La copie de test est protégée par mot de passe et bloquée aux robots.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
