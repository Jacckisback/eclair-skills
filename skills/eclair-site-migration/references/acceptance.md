# Plan de validation — Changement d'hébergeur ou de domaine

## Modèle de données
Sauvegarde, nouvel hébergement, DNS, redirections de domaine.

## Mise en œuvre attendue
Sauvegarder, restaurer chez le nouvel hébergeur, vérifier, basculer le DNS, rediriger l'ancien domaine page à page.

## Tests à prévoir
1. Nominal : Répéter le déménagement sur un domaine de test.
2. Contrôle de refus : Aucune ancienne adresse ne répond en 404 après la bascule.
3. Invariant : Les secrets du site ne voyagent jamais par e-mail ou messagerie.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
