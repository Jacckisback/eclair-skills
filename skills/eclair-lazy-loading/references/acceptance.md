# Plan de validation — Chargement différé

## Modèle de données
Image, priorité, dimensions.

## Mise en œuvre attendue
Vérifier que l'image principale est chargée en priorité et les autres en différé, avec dimensions explicites.

## Tests à prévoir
1. Nominal : Mesurer l'affichage du plus grand élément et le décalage de mise en page.
2. Contrôle de refus : L'image principale n'est jamais chargée en différé.
3. Invariant : Aucun script tiers n'est ajouté pour différer le chargement.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
