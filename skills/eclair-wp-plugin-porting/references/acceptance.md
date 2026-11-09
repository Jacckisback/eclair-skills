# Plan de validation — Portage d'extensions WordPress

## Modèle de données
Extension d'origine, fonctions réellement utilisées, équivalent natif, écart.

## Mise en œuvre attendue
Lister ce que l'extension fait vraiment sur le site, chercher d'abord la fonction native, sinon le skill du catalogue, sinon une extension sur mesure ; ne jamais copier de code PHP WordPress.

## Tests à prévoir
1. Nominal : Dresser la table de correspondance d'un site réel et la faire valider.
2. Contrôle de refus : Une fonction sans équivalent est annoncée comme manquante, pas simulée.
3. Invariant : Aucun code sous licence incompatible ou dépendant de l'API WordPress n'est repris.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
