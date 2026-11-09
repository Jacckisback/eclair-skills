# Plan de validation — Liens affiliés

## Modèle de données
Lien, programme, mention, contenu porteur.

## Mise en œuvre attendue
Activer la fonction d'affiliation livrée, déclarer les programmes, laisser le noyau ajouter mention et attribut sponsorisé.

## Tests à prévoir
1. Nominal : Publier un comparatif et vérifier mention et attributs des liens.
2. Contrôle de refus : Un lien affilié n'est jamais présenté comme un avis indépendant.
3. Invariant : Aucun lien affilié sans mention publicitaire visible.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
