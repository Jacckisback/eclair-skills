# Plan de validation — Signaux web essentiels

## Modèle de données
Affichage du plus grand élément, stabilité, réactivité, par gabarit.

## Mise en œuvre attendue
Mesurer en laboratoire et sur données réelles quand elles existent, traiter la cause principale par gabarit, re-mesurer.

## Tests à prévoir
1. Nominal : Mesurer trois gabarits sur mobile avant et après correction.
2. Contrôle de refus : Une amélioration non mesurée n'est pas annoncée comme acquise.
3. Invariant : Aucun score n'est promis ; seuls les résultats mesurés sont rapportés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
