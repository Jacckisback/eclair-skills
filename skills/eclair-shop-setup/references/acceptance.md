# Plan de validation — Ouverture de la boutique légère

## Modèle de données
Produit, prix, catégorie, mentions légales, conditions de vente.

## Mise en œuvre attendue
Publier mentions légales et conditions de vente, ouvrir la boutique, créer les premières fiches, vérifier catalogue et données structurées.

## Tests à prévoir
1. Nominal : Ouvrir la boutique sur une copie et parcourir catalogue et fiche.
2. Contrôle de refus : La boutique ne s'ouvre pas sans pages légales publiées.
3. Invariant : Aucun prix, délai ou condition de vente inventés par l'agent.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
