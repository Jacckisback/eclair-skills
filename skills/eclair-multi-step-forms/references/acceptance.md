# Plan de validation — Formulaires en plusieurs étapes

## Modèle de données
Étape, champs, validation, brouillon de réponse.

## Mise en œuvre attendue
Découper par thème, valider côté serveur à chaque étape, prévoir reprise et récapitulatif avant envoi.

## Tests à prévoir
1. Nominal : Remplir, revenir en arrière, corriger et envoyer.
2. Contrôle de refus : Une étape invalide bloque la suite et aucune donnée incomplète n'est transmise.
3. Invariant : Aucune donnée partielle n'est conservée sans information de la personne.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
