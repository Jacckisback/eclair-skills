# Plan de validation — API publique en lecture

## Modèle de données
Ressource, champs publics, pagination, version.

## Mise en œuvre attendue
Déclarer des routes GET cacheables qui renvoient du JSON borné et versionné ; documenter que l'écriture n'est pas ouverte.

## Tests à prévoir
1. Nominal : Lire liste et détail, pagination et cas vide.
2. Contrôle de refus : Un contenu non publié n'est renvoyé par aucune route.
3. Invariant : Seuls des contenus déjà publics sont exposés ; aucun identifiant interne sensible.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
