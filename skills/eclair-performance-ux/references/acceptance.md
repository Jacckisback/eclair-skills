# Plan de validation — Performance UX

## Modèle de données
LCP, CLS, INP, poids d’assets, CSS, JS, cache et polices.

## Implémentation attendue
Mesurer avant/après via tools/measure.php --check, Chrome Lighthouse et réseau lent, optimiser images et scripts.

## Tests à prévoir
1. Nominal : Tester site public sans extension, avec extension et sur mobile.
2. Contrôle de refus : Une amélioration déclarée est accompagnée de mesures reproductibles avant/après.
3. Invariant : Ne pas dégrader le chemin de cache PHP ni désactiver CSP pour gagner en facilité.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
