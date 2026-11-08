# Plan de validation — Catalogue produits

## Modèle de données
Produit, SKU, slug, titre, description, prix de présentation, média, disponibilité et catégorie.

## Implémentation attendue
Prototyper d’abord une page publique GET cacheable; produire un schéma produit et son index; garder titres et descriptions source; définir pagination et canonical; préserver les slugs au fil des éditions.

## Tests à prévoir
1. Nominal : Tester catégories, listes vides, URL canonique, recherche et suppression soft.
2. Contrôle de refus : Un produit supprimé ou privé ne doit pas demeurer dans le catalogue ni dans un ancien cache.
3. Invariant : Le prix affiché n’est jamais pris comme source d’autorité lors d’une future commande.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
