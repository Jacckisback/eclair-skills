# Plan de validation — Abonnements et adhésions

## Modèle de données
Plan, adhésion, renouvellement, période, résiliation, paiement, droit.

## Implémentation attendue
Calculer droits depuis l’état vérifié, prévoir changements de plan et périodes de grâce, traiter événements de facturation de façon idempotente.

## Tests à prévoir
1. Nominal : Tester échec prélèvement, prorata, remboursement et résiliation.
2. Contrôle de refus : Deux événements identiques ne prolongent pas l’abonnement deux fois.
3. Invariant : Un reçu navigateur ne suffit jamais pour renouveler un accès payant.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
