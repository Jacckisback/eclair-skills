# Plan de validation — Observabilité et alertes

## Modèle de données
Logs structurés, erreurs, corrélations, métriques, traces, rétention.

## Implémentation attendue
Définir alertes utiles, anonymiser données, surveiller tâches et cache, distinguer incident site et module, fournir runbook.

## Tests à prévoir
1. Nominal : Tester hausse erreurs 5xx, retard des tâches et disque plein.
2. Contrôle de refus : Un module désactivé ne continue pas à envoyer de données ni à exécuter de tâches.
3. Invariant : Aucun mot de passe, jeton, paiement ou PII brute dans les logs; pas de télémétrie cachée.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
