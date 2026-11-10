# Plan de validation — Sujets et réponses

## Modèle de données
Sujet, réponse, version, auteur, horodatage, épinglé, fermé, supprimé.

## Mise en œuvre attendue
Définir parenté de réponses, pagination, historique des éditions, mentions et permaliens; traiter envois idempotents.

## Tests à prévoir
1. Nominal : Tester réponses concurrentes, message effacé et sujet fermé.
2. Contrôle de refus : Un membre ne peut pas éditer ni supprimer la réponse d’un autre sans droit explicite.
3. Invariant : Échapper Markdown/HTML et vérifier permission d’éditer pour chaque publication.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
