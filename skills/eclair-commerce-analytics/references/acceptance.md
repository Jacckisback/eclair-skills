# Plan de validation — Mesure des ventes

## Modèle de données
Entonnoir, commandes confirmées, remboursements, taux de conversion, revenus nets, consentements.

## Mise en œuvre attendue
Définir événements et métriques sans réutiliser des données sensibles; rapprocher totaux de commande, avoirs et paiements; prévoir une synthèse agrégée.

## Tests à prévoir
1. Nominal : Tester revenus après remboursement et rupture de comptage.
2. Contrôle de refus : L’agrégation ne doit ni compter deux fois le même paiement ni divulguer une commande identifiable.
3. Invariant : Les données analytiques personnelles exigent base légale et ne doivent pas fuiter via le cache.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
