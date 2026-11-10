# Plan de validation — Observabilité et alertes

## Modèle de données
Logs structurés, erreurs, corrélations, métriques, traces, rétention.

## Mise en œuvre attendue
Définir alertes utiles, anonymiser données, surveiller tâches et cache, distinguer incident site et module, fournir runbook.

## Tests à prévoir
1. Nominal : Tester hausse erreurs 5xx, retard des tâches et disque plein.
2. Contrôle de refus : Un module désactivé ne continue pas à envoyer de données ni à exécuter de tâches.
3. Invariant : Aucun mot de passe, jeton, paiement ou PII brute dans les logs; pas de télémétrie cachée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
