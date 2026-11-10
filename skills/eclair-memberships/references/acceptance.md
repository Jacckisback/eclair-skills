# Plan de validation — Abonnements et adhésions

## Modèle de données
Plan, adhésion, renouvellement, période, résiliation, paiement, droit.

## Mise en œuvre attendue
Calculer droits depuis l’état vérifié, prévoir changements de plan et périodes de grâce, traiter événements de facturation de façon idempotente.

## Tests à prévoir
1. Nominal : Tester échec prélèvement, prorata, remboursement et résiliation.
2. Contrôle de refus : Deux événements identiques ne prolongent pas l’abonnement deux fois.
3. Invariant : Un reçu navigateur ne suffit jamais pour renouveler un accès payant.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
