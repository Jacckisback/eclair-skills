# Plan de validation — Migration WordPress

## Modèle de données
Export WordPress, IDs anciens, slugs, médias, catégories, auteurs, redirections et requêtes ?p=.

## Implémentation attendue
Utiliser la fonction native WordPress; inventorier URLs historiques, simuler import, comparer slug/canonical, conserver liens exacts et médias, fournir plan rollback.

## Tests à prévoir
1. Nominal : Tester URL avec slash final, query alias, accents, images et pages supprimées.
2. Contrôle de refus : Pour chaque URL indexée ancienne, obtenir 200 exact ou redirection 301 ciblée.
3. Invariant : Éviter des 404 et suppressions d’URLs; jamais de bascule DNS sans tests et sauvegardes.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
