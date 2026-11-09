# Plan de validation — Connexion par compte tiers

## Modèle de données
Fournisseur d'identité, compte lié, consentement.

## Mise en œuvre attendue
Dépend d'abord de comptes membres ; concevoir le flux OAuth avec état, PKCE et liaison de compte explicite.

## Tests à prévoir
1. Nominal : Simuler connexion, liaison et déliaison.
2. Contrôle de refus : Une réponse OAuth rejouée ou falsifiée est refusée.
3. Invariant : Aucun compte n'est fusionné sur la seule foi d'une adresse e-mail non vérifiée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
