# Plan de validation — SEO multilingue

## Modèle de données
Langue, URL de traduction, hreflang réciproque, titre et sitemap.

## Implémentation attendue
Inventorier langues publiées, définir mapping de traductions, tester canonical par langue, hreflang/x-default et absence de redirection intrusive.

## Tests à prévoir
1. Nominal : Tester paires FR/ES/EN, pages manquantes et changement de langue.
2. Contrôle de refus : Chaque lien hreflang pointe vers une URL 200 indexable et réciproque.
3. Invariant : Ne pas utiliser une traduction automatique non vérifiée comme page définitive.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
