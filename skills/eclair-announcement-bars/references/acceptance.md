# Plan de validation — Bandeaux d'annonce

## Modèle de données
Message, lien, dates de début et de fin.

## Mise en œuvre attendue
Rendre le bandeau côté serveur avec dates de validité, sans décalage de mise en page, retiré automatiquement à l'échéance.

## Tests à prévoir
1. Nominal : Afficher, fermer et laisser expirer un bandeau.
2. Contrôle de refus : Après la date de fin, le bandeau n'apparaît plus sur aucune page.
3. Invariant : Aucune annonce expirée ne reste servie par le cache.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
