# Plan de validation — Connecteurs API

## Modèle de données
OAuth/token, scopes, quotas, erreurs, pagination, version et journaux.

## Implémentation attendue
Définir schéma d’API, isoler secrets, valider schémas entrants, prévoir timeouts/circuit breaker et versionning.

## Tests à prévoir
1. Nominal : Tester timeout, 429, 500, réponse malformée et révocation.
2. Contrôle de refus : Un 500 du fournisseur n’endommage pas les données locales ni le rendu public.
3. Invariant : Ne pas autoriser SSRF ou URLs dynamiques arbitraires; ne jamais journaliser token.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
