# Plan de validation — SEO multilingue

## Modèle de données
Langue, URL de traduction, hreflang réciproque, titre et sitemap.

## Mise en œuvre attendue
Inventorier langues publiées, définir mapping de traductions, tester canonical par langue, hreflang/x-default et absence de redirection intrusive.

## Tests à prévoir
1. Nominal : Tester paires FR/ES/EN, pages manquantes et changement de langue.
2. Contrôle de refus : Chaque lien hreflang pointe vers une URL 200 indexable et réciproque.
3. Invariant : Ne pas utiliser une traduction automatique non vérifiée comme page définitive.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
