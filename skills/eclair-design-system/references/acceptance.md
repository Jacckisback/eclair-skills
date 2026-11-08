# Plan de validation — Système de design

## Modèle de données
Tokens, grille, espacements, couleurs, typographie, composants et états.

## Implémentation attendue
Déclarer échelle des tokens, réutiliser composants, documenter états et variantes; compatibilité thème Éclair.

## Tests à prévoir
1. Nominal : Tester contraste, cohérence et changement de thème.
2. Contrôle de refus : Changer la couleur principale ne crée aucune illisibilité des liens ou erreurs.
3. Invariant : Ne pas introduire de feuille CSS lourde ou de bibliothèque JS sans preuve de besoin.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
