# Plan de validation — Notifications de communauté

## Modèle de données
Abonnement, mention, notification, canal, préférence, statut.

## Mise en œuvre attendue
Émettre événements après écriture validée, filtrer par droits au moment de la lecture et de l’envoi, appliquer désabonnement.

## Tests à prévoir
1. Nominal : Tester notifications répétées, désabonnement et retrait de permission.
2. Contrôle de refus : Après révocation d’accès, aucune nouvelle notification ne contient un extrait privé.
3. Invariant : Ne jamais révéler contenu de catégories privées dans email push ou digest.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
