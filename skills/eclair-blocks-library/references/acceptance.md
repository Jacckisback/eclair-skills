# Plan de validation — Bibliothèque de blocs

## Modèle de données
Type namespacé, déclaration des champs, limites, rendu et données conservées.

## Implémentation attendue
Privilégier blocs natifs; déclarer champs autorisés; générer rendu échappé, valeurs par défaut et préservation après désactivation.

## Tests à prévoir
1. Nominal : Tester champs invalides, suppression de la fonction et réinstallation.
2. Contrôle de refus : Le bloc désactivé est conservé mais ni exécuté ni rendu.
3. Invariant : Refuser l’exécution de HTML/JS issu de champs; aucune perte de données lorsque le bloc manque.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
