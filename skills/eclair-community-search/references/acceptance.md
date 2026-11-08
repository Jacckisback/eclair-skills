# Plan de validation — Recherche de forum

## Modèle de données
Terme, index borné, langue, catégorie, page, statut et droits.

## Implémentation attendue
Normaliser texte, indexer les publications autorisées, paginer et limiter coût, retirer du résultat les objets supprimés.

## Tests à prévoir
1. Nominal : Tester phrase vide, injection, recherche massive, sujets privés.
2. Contrôle de refus : Un visiteur ne doit pas voir l’extrait d’une discussion privée dans une suggestion.
3. Invariant : Le filtrage des permissions intervient à chaque recherche, pas seulement au moment de l’indexation.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
