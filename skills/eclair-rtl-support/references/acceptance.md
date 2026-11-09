# Plan de validation — Langues de droite à gauche

## Modèle de données
Direction du texte, propriétés logiques CSS, icônes orientées.

## Mise en œuvre attendue
Utiliser les propriétés logiques CSS dans le thème de site, tester chaque gabarit en dir=rtl.

## Tests à prévoir
1. Nominal : Afficher les pages types en droite à gauche sans débordement.
2. Contrôle de refus : Un mélange de langues ne casse pas l'ordre de lecture.
3. Invariant : Aucun texte utilisateur n'est injecté sans échappement, y compris les caractères de direction.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
