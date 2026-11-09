# Plan de validation — Boutons de partage

## Modèle de données
Réseau, adresse de partage, libellé.

## Mise en œuvre attendue
Utiliser de simples liens de partage et l'API de partage du navigateur en amélioration progressive.

## Tests à prévoir
1. Nominal : Partager une page depuis mobile et ordinateur.
2. Contrôle de refus : Aucune requête tierce avant le clic.
3. Invariant : Aucun bouton ne charge de script ou de traceur tiers.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
