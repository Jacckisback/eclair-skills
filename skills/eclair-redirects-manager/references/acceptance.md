# Plan de validation — Redirections

## Modèle de données
Ancienne adresse, nouvelle adresse, type, date.

## Mise en œuvre attendue
Importer les anciennes adresses, créer une redirection directe par adresse, supprimer chaînes et boucles.

## Tests à prévoir
1. Nominal : Tester un lot d'anciennes adresses et relever statut et destination.
2. Contrôle de refus : Aucune chaîne de plus d'un saut ni boucle.
3. Invariant : Aucune redirection ouverte vers un domaine non voulu.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
