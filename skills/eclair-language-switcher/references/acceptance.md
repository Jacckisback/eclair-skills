# Plan de validation — Sélecteur de langue

## Modèle de données
Langue courante, versions disponibles, libellés.

## Mise en œuvre attendue
Lister les langues par leur nom dans leur propre langue, pointer vers la version équivalente, sans redirection automatique forcée.

## Tests à prévoir
1. Nominal : Changer de langue depuis une page profonde et arriver sur son équivalent.
2. Contrôle de refus : Sans équivalent, le lien mène à l'accueil de la langue, pas à une erreur.
3. Invariant : Aucune redirection par adresse IP ; le choix du visiteur est respecté.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
