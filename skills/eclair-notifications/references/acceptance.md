# Plan de validation — Notifications de communauté

## Modèle de données
Abonnement, mention, notification, canal, préférence, statut.

## Implémentation attendue
Émettre événements après écriture validée, filtrer par droits au moment de la lecture et de l’envoi, appliquer désabonnement.

## Tests à prévoir
1. Nominal : Tester notifications répétées, désabonnement et retrait de permission.
2. Contrôle de refus : Après révocation d’accès, aucune nouvelle notification ne contient un extrait privé.
3. Invariant : Ne jamais révéler contenu de catégories privées dans email push ou digest.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
