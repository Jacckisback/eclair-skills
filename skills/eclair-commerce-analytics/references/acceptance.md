# Plan de validation — Mesure des ventes

## Modèle de données
Entonnoir, commandes confirmées, remboursements, taux de conversion, revenus nets, consentements.

## Implémentation attendue
Définir événements et métriques sans réutiliser des données sensibles; rapprocher totaux de commande, avoirs et paiements; prévoir une synthèse agrégée.

## Tests à prévoir
1. Nominal : Tester revenus après remboursement et rupture de comptage.
2. Contrôle de refus : L’agrégation ne doit ni compter deux fois le même paiement ni divulguer une commande identifiable.
3. Invariant : Les données analytiques personnelles exigent base légale et ne doivent pas fuiter via le cache.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
