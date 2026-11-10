# Plan de validation — Promotions et coupons

## Modèle de données
Code, budget, dates, quota, conditions de panier, usages et exclusions.

## Mise en œuvre attendue
Définir ordre de calcul et arrondi; vérifier coupon avant commande; décompter les usages atomiquement; tracer annulation et retour.

## Tests à prévoir
1. Nominal : Tester coupons expirés, épuisés, seuil et exclusions.
2. Contrôle de refus : Deux commandes simultanées ne peuvent pas consommer le dernier coupon unique.
3. Invariant : La décision d’éligibilité vient des données serveur et non de la réduction saisie en HTML.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
