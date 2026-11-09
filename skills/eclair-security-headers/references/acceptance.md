# Plan de validation — En-têtes de sécurité

## Modèle de données
En-têtes HTTP, Content-Security-Policy, HTTPS.

## Mise en œuvre attendue
Relever les en-têtes servis, vérifier HTTPS partout, tester les règles du serveur web livrées avec le noyau.

## Tests à prévoir
1. Nominal : Analyser les en-têtes d'une page publique et de l'administration.
2. Contrôle de refus : Un fichier sensible ou de données n'est jamais servi par le serveur web.
3. Invariant : Aucun en-tête de protection n'est retiré ni assoupli.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
