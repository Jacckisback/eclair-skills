# Plan de validation — Connecteurs API

## Modèle de données
OAuth/token, scopes, quotas, erreurs, pagination, version et journaux.

## Mise en œuvre attendue
Définir schéma d’API, isoler secrets, valider schémas entrants, prévoir timeouts/circuit breaker et versionning.

## Tests à prévoir
1. Nominal : Tester timeout, 429, 500, réponse malformée et révocation.
2. Contrôle de refus : Un 500 du fournisseur n’endommage pas les données locales ni le rendu public.
3. Invariant : Ne pas autoriser SSRF ou URLs dynamiques arbitraires; ne jamais journaliser token.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
