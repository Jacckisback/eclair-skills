# Plan de validation — Accessibilité WCAG

## Modèle de données
Structure des titres, navigation clavier, focus, formulaires, médias, contrastes.

## Mise en œuvre attendue
Réaliser audit clavier et lecteur d’écran, vérifier axe-core, contrastes, messages d’erreur et mouvement réduit.

## Tests à prévoir
1. Nominal : Tester parcours sans souris, erreurs de formulaire et zoom 200%.
2. Contrôle de refus : Un formulaire reste compréhensible sans couleur et depuis le clavier.
3. Invariant : Ne pas supprimer focus visible ou rendre une fonction dépendante uniquement de couleur ou geste.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
