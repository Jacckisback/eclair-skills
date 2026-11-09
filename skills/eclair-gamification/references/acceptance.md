# Plan de validation — Badges et points

## Modèle de données
Règle, points, badge, classement.

## Mise en œuvre attendue
Fixer des règles simples et vérifiables côté serveur, prévoir retrait en cas d'abus et option de ne pas apparaître au classement.

## Tests à prévoir
1. Nominal : Simuler gain, retrait et affichage du classement.
2. Contrôle de refus : Une action répétée artificiellement ne rapporte pas de points en double.
3. Invariant : Aucun point n'est attribué sur la foi d'une information envoyée par le navigateur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
