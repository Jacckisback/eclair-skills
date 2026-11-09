# Plan de validation — Diaporamas et carrousels

## Modèle de données
Diapositive, image, texte, lien, ordre.

## Mise en œuvre attendue
Préférer une image forte unique ; sinon défilement CSS avec commandes clavier, pause et aucune lecture automatique imposée.

## Tests à prévoir
1. Nominal : Naviguer au clavier et au lecteur d'écran, mesurer le décalage de mise en page.
2. Contrôle de refus : Sans JavaScript, tout le contenu des diapositives reste lisible.
3. Invariant : Aucune bibliothèque tierce lourde ; respect de prefers-reduced-motion.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
