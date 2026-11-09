# Plan de validation — Magazine et actualités

## Modèle de données
Article, rubrique, auteur, une, date.

## Mise en œuvre attendue
Structurer rubriques et une, soigner auteurs et dates, utiliser les fonctions natives pour les médias (grandes images, planning, flux).

## Tests à prévoir
1. Nominal : Publier une une de test et vérifier rubriques, flux et sitemap.
2. Contrôle de refus : Un article corrigé affiche sa date de mise à jour.
3. Invariant : Aucune information non sourcée présentée comme un fait.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
