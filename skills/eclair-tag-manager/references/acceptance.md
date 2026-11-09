# Plan de validation — Gestionnaire de balises

## Modèle de données
Conteneur, balises, déclencheurs, consentement.

## Mise en œuvre attendue
Lister les balises réellement nécessaires, chercher une alternative côté serveur, documenter le blocage par la politique de contenu native.

## Tests à prévoir
1. Nominal : Dresser l'inventaire des balises et leur alternative.
2. Contrôle de refus : Une balise non justifiée n'est pas ajoutée.
3. Invariant : Aucun conteneur permettant d'injecter du code arbitraire sans relecture.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
