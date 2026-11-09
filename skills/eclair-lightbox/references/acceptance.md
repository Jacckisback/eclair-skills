# Plan de validation — Visionneuse d'images

## Modèle de données
Image, version agrandie, légende.

## Mise en œuvre attendue
Utiliser dialog natif ou lien vers l'image, gérer focus, touche Échap et retour, sans dépendance.

## Tests à prévoir
1. Nominal : Ouvrir, naviguer et fermer au clavier.
2. Contrôle de refus : Sans JavaScript, le clic ouvre simplement l'image.
3. Invariant : Le focus est piégé puis rendu correctement ; aucun contenu externe.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
