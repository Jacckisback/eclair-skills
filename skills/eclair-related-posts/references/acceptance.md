# Plan de validation — Contenus associés

## Modèle de données
Contenu, catégorie, mots communs, liste de liens calculée.

## Mise en œuvre attendue
Calculer les associations à la publication ou par tâche, les rendre par un bloc statique cacheable, limiter à quelques liens.

## Tests à prévoir
1. Nominal : Vérifier les liens proposés sur plusieurs articles de catégories différentes.
2. Contrôle de refus : Un article supprimé n'est plus proposé après régénération.
3. Invariant : Aucune association ne pointe vers un contenu non publié.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
