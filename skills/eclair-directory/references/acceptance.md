# Plan de validation — Annuaire professionnel

## Modèle de données
Fiche, catégorie, localisation, contact public, statut de vérification.

## Mise en œuvre attendue
Séparer données professionnelles publiques et privées; créer pages catégorie, canonical, modération et filtres bornés.

## Tests à prévoir
1. Nominal : Tester fausses fiches, doublons, suppression et recherche vide.
2. Contrôle de refus : Une fiche en attente n’apparaît ni dans le sitemap ni dans les données structurées.
3. Invariant : Ne pas publier adresse personnelle, téléphone ou coordonnées sensibles sans autorisation.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
