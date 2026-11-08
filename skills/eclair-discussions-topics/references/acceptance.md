# Plan de validation — Sujets et réponses

## Modèle de données
Sujet, réponse, version, auteur, horodatage, épinglé, fermé, supprimé.

## Implémentation attendue
Définir parenté de réponses, pagination, historique des éditions, mentions et permaliens; traiter envois idempotents.

## Tests à prévoir
1. Nominal : Tester réponses concurrentes, message effacé et sujet fermé.
2. Contrôle de refus : Un membre ne peut pas éditer ni supprimer la réponse d’un autre sans droit explicite.
3. Invariant : Échapper Markdown/HTML et vérifier permission d’éditer pour chaque publication.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
