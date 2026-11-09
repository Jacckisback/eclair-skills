# Plan de validation — Articles de blog

## Modèle de données
Article, extrait, image principale, catégorie, auteur, date, statut brouillon ou publié.

## Mise en œuvre attendue
Créer les articles en brouillon par l'administration ou le connecteur MCP, vérifier titre, extrait, image et catégorie, puis laisser une personne publier.

## Tests à prévoir
1. Nominal : Créer un brouillon complet, le faire publier, puis vérifier son rendu, le flux RSS et le sitemap.
2. Contrôle de refus : Un brouillon n'apparaît ni sur le site public, ni dans le sitemap, ni dans le flux.
3. Invariant : Ne jamais publier ni supprimer un contenu à la place de la personne autorisée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
