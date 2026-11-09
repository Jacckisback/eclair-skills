# Plan de validation — Réglages du site

## Modèle de données
Nom, description, logo, coordonnées, langue, thème, direction artistique.

## Mise en œuvre attendue
Lire les capacités du site, renseigner les réglages par l'administration, prévisualiser avant d'enregistrer.

## Tests à prévoir
1. Nominal : Régler un site neuf et vérifier le rendu public.
2. Contrôle de refus : Un compte sans droit Réglages ne modifie aucun réglage.
3. Invariant : Aucune protection native n'est désactivée pour gagner du temps.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
