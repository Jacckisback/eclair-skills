# Plan de validation — Commandes et paiements

## Modèle de données
Commande, tentative de paiement, identifiant fournisseur, preuve webhook, idempotency key, remboursement.

## Implémentation attendue
Détailler les transitions autorisées; stocker la preuve de la notification et son horodatage; traiter webhook durablement; prévoir reconciliation et remboursement partiel.

## Tests à prévoir
1. Nominal : Tester webhook inversé, hors ordre, réémis et paiement refusé.
2. Contrôle de refus : Un webhook sans signature valide ne modifie ni commande ni accès LMS.
3. Invariant : Ne jamais stocker données de carte bancaire brutes; checkout hébergé chez le prestataire et signature des webhooks vérifiée.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
