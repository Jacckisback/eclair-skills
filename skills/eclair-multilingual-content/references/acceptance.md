# Plan de validation — Contenus multilingues

## Modèle de données
Contenu, langue, version liée, adresse par langue.

## Mise en œuvre attendue
Vérifier les langues prises en charge par le site dans les capacités, organiser une arborescence par langue, relier les versions et contrôler hreflang.

## Tests à prévoir
1. Nominal : Créer une page en deux langues et vérifier liens croisés et hreflang.
2. Contrôle de refus : Une langue sans traduction ne renvoie pas vers une page vide.
3. Invariant : Aucune traduction automatique publiée sans relecture humaine.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
