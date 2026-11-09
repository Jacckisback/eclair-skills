# Plan de validation — Recettes

## Modèle de données
Recette, ingrédients, étapes, temps, portions.

## Mise en œuvre attendue
Structurer chaque recette en ingrédients et étapes, ajouter temps et portions, prévoir une version imprimable.

## Tests à prévoir
1. Nominal : Suivre une recette publiée sur mobile et l'imprimer.
2. Contrôle de refus : Une recette sans quantités n'est pas publiée.
3. Invariant : Aucune allégation de santé non étayée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
