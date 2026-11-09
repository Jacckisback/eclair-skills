# Plan de validation — Sections d'en-tête

## Modèle de données
Titre, sous-titre, image, bouton.

## Mise en œuvre attendue
Écrire une promesse précise, choisir une image légère, garder un seul titre principal et un bouton.

## Tests à prévoir
1. Nominal : Mesurer l'affichage du plus grand élément sur mobile.
2. Contrôle de refus : Sans image, la section reste lisible et contrastée.
3. Invariant : L'image principale a des dimensions explicites et ne retarde pas l'affichage.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
