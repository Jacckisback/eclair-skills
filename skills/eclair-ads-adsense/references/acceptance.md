# Plan de validation — Publicité

## Modèle de données
Emplacement, consentement, fichier ads.txt.

## Mise en œuvre attendue
Utiliser la page Publicité native, limiter les emplacements, vérifier consentement, étiquette et impact sur la vitesse.

## Tests à prévoir
1. Nominal : Mesurer la page avec et sans publicité et vérifier le consentement.
2. Contrôle de refus : Les pages hors articles n'affichent pas de publicité.
3. Invariant : Aucune publicité chargée avant le consentement requis.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
