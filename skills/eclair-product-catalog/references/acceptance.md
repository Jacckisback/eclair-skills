# Plan de validation — Catalogue produits

## Modèle de données
Produit, SKU, slug, titre, description, prix de présentation, média, disponibilité et catégorie.

## Mise en œuvre attendue
Prototyper d’abord une page publique GET cacheable; produire un schéma produit et son index; garder titres et descriptions source; définir pagination et canonical; préserver les slugs au fil des éditions.

## Tests à prévoir
1. Nominal : Tester catégories, listes vides, URL canonique, recherche et suppression soft.
2. Contrôle de refus : Un produit supprimé ou privé ne doit pas demeurer dans le catalogue ni dans un ancien cache.
3. Invariant : Le prix affiché n’est jamais pris comme source d’autorité lors d’une future commande.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
