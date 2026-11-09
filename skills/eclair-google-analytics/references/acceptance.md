# Plan de validation — Google Analytics

## Modèle de données
Identifiant de mesure, consentement, événements.

## Mise en œuvre attendue
Vérifier d'abord si une mesure sans cookie suffit ; sinon consentement préalable, et constat que la politique de contenu native n'est pas ouverte aux extensions.

## Tests à prévoir
1. Nominal : Vérifier l'absence de requête avant consentement.
2. Contrôle de refus : Après refus, aucune donnée n'est envoyée.
3. Invariant : Aucun script de mesure chargé avant consentement ni en contournant la Content-Security-Policy.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
