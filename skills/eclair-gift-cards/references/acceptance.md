# Plan de validation — Cartes cadeaux

## Modèle de données
Carte, code, solde, validité.

## Mise en œuvre attendue
Générer des codes imprévisibles, suivre le solde côté serveur, traiter l'expiration selon la loi applicable.

## Tests à prévoir
1. Nominal : Simuler achat, utilisation partielle et solde restant.
2. Contrôle de refus : Un code épuisé ou expiré est refusé.
3. Invariant : Un code n'est jamais devinable ni réutilisable au-delà de son solde.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
