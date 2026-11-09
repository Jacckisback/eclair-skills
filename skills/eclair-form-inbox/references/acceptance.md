# Plan de validation — Messages reçus

## Modèle de données
Message, statut, réponse, durée de conservation.

## Mise en œuvre attendue
Définir qui lit et répond, sous quel délai, combien de temps les messages sont conservés, comment ils sont supprimés.

## Tests à prévoir
1. Nominal : Traiter un message de la réception à l'archivage.
2. Contrôle de refus : Un compte sans le droit Messages n'accède à aucun message.
3. Invariant : Durée de conservation limitée et droit d'accès restreint.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
