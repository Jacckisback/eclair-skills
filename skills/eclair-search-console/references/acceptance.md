# Plan de validation — Search Console

## Modèle de données
Propriété, méthode de vérification, sitemap déclaré, rapports.

## Mise en œuvre attendue
Vérifier le domaine par enregistrement DNS, déclarer le sitemap natif, lire couverture et requêtes chaque mois.

## Tests à prévoir
1. Nominal : Vérifier la propriété et la prise en compte du sitemap.
2. Contrôle de refus : Une erreur de couverture est expliquée, pas masquée.
3. Invariant : Aucun accès propriétaire donné à un tiers sans accord du client.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
