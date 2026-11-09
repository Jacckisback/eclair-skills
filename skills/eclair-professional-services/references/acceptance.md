# Plan de validation — Site de profession libérale

## Modèle de données
Prestation, praticien, honoraires indicatifs, prise de contact.

## Mise en œuvre attendue
Présenter domaines d'intervention et parcours réels, respecter les règles de communication de la profession, proposer contact ou rendez-vous.

## Tests à prévoir
1. Nominal : Faire relire les contenus par le professionnel.
2. Contrôle de refus : Une spécialité non reconnue n'est pas affichée comme titre.
3. Invariant : Aucune promesse de résultat ni mention interdite par la déontologie de la profession.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
