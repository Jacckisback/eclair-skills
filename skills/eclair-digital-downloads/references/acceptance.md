# Plan de validation — Produits numériques

## Modèle de données
Produit numérique, achat, lien de livraison temporaire.

## Mise en œuvre attendue
Faire livrer le fichier par le prestataire ou par lien signé à durée limitée ; ne jamais placer le fichier à une adresse publique.

## Tests à prévoir
1. Nominal : Simuler achat, livraison et expiration du lien.
2. Contrôle de refus : Un lien expiré ou partagé ne donne plus accès au fichier.
3. Invariant : Aucun fichier payant n'est accessible sans achat vérifié.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
