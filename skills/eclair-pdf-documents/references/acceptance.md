# Plan de validation — Documents PDF

## Modèle de données
Document, titre, résumé, page de présentation, fichier.

## Mise en œuvre attendue
Créer une page HTML de présentation par document avec résumé, lien de téléchargement et alternative accessible.

## Tests à prévoir
1. Nominal : Vérifier lien, poids, titre du document et page de présentation.
2. Contrôle de refus : Un PDF retiré renvoie une réponse propre et non un lien cassé dans les pages.
3. Invariant : Aucun PDF contenant des données personnelles n'est publié sans accord.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
