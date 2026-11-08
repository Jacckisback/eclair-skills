# Plan de validation — Variantes et attributs

## Modèle de données
Produit parent, variantes à SKU unique, combinaisons d’attributs, prix/stock propres, média et statut.

## Implémentation attendue
Définir le nombre maximal de combinaisons; assurer unicité SKU; projeter variantes dans le rendu GET; préparer sélection validée au serveur lors du checkout.

## Tests à prévoir
1. Nominal : Tester variantes absentes, épuisées et désactivées.
2. Contrôle de refus : Deux combinaisons créent le même SKU => refus explicite avant publication.
3. Invariant : Ne jamais accepter prix, poids ou stock envoyés par le navigateur comme données fiables.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
