# Plan de validation — Appels à l'action

## Modèle de données
Titre, texte, bouton, destination.

## Mise en œuvre attendue
Définir une action principale par page, la répéter aux bons endroits, vérifier contraste et libellé explicite.

## Tests à prévoir
1. Nominal : Suivre chaque bouton jusqu'à sa destination sur mobile.
2. Contrôle de refus : Un bouton sans destination valide n'est pas publié.
3. Invariant : Aucun lien trompeur ni redirection ouverte.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
