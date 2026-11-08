# Plan de validation — Promotions et coupons

## Modèle de données
Code, budget, dates, quota, conditions de panier, usages et exclusions.

## Implémentation attendue
Définir ordre de calcul et arrondi; vérifier coupon avant commande; décompter les usages atomiquement; tracer annulation et retour.

## Tests à prévoir
1. Nominal : Tester coupons expirés, épuisés, seuil et exclusions.
2. Contrôle de refus : Deux commandes simultanées ne peuvent pas consommer le dernier coupon unique.
3. Invariant : La décision d’éligibilité vient des données serveur et non de la réduction saisie en HTML.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
