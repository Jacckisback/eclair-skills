# Plan de validation — FAQ et accordéons

## Modèle de données
Question, réponse, ordre.

## Mise en œuvre attendue
Rédiger de vraies questions de clients, utiliser le bloc FAQ natif qui produit aussi le balisage, limiter le nombre par page.

## Tests à prévoir
1. Nominal : Vérifier ouverture au clavier et balisage produit.
2. Contrôle de refus : Une FAQ vide n'émet aucun balisage.
3. Invariant : Aucune réponse inventée ou promesse non vérifiée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
