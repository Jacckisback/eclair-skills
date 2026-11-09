# Plan de validation — Sondages et enquêtes

## Modèle de données
Question, choix, réponse, participant anonyme, résultats agrégés.

## Mise en œuvre attendue
Définir anonymat, limitation des votes multiples, affichage des résultats agrégés et durée du sondage.

## Tests à prévoir
1. Nominal : Voter, consulter les résultats et clôturer le sondage.
2. Contrôle de refus : Un second vote du même participant est ignoré.
3. Invariant : Aucune réponse individuelle n'est publiée ; résultats agrégés seulement.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
