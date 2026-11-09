# Plan de validation — Avis sur les produits

## Modèle de données
Avis, note, auteur, achat vérifié, statut.

## Mise en œuvre attendue
Définir preuve d'achat, modération, droit de réponse et affichage agrégé ; proposer d'ici là des témoignages recueillis manuellement.

## Tests à prévoir
1. Nominal : Simuler dépôt, modération et publication d'un avis.
2. Contrôle de refus : Un avis sans achat vérifié n'est pas marqué comme vérifié.
3. Invariant : Aucun avis publié sans modération ; aucune note agrégée sans avis réels.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
