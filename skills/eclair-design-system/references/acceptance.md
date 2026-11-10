# Plan de validation — Système de design

## Modèle de données
Tokens, grille, espacements, couleurs, typographie, composants et états.

## Mise en œuvre attendue
Déclarer échelle des tokens, réutiliser composants, documenter états et variantes; compatibilité thème Éclair.

## Tests à prévoir
1. Nominal : Tester contraste, cohérence et changement de thème.
2. Contrôle de refus : Changer la couleur principale ne crée aucune illisibilité des liens ou erreurs.
3. Invariant : Ne pas introduire de feuille CSS lourde ou de bibliothèque JS sans preuve de besoin.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
