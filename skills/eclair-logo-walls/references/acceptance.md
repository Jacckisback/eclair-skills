# Plan de validation — Logos clients et partenaires

## Modèle de données
Logo, nom, lien facultatif.

## Mise en œuvre attendue
Afficher les logos en grille statique, tailles homogènes, noms en texte alternatif.

## Tests à prévoir
1. Nominal : Vérifier lisibilité en mode clair et sombre.
2. Contrôle de refus : Un logo sans autorisation consignée n'est pas intégré.
3. Invariant : Seuls les logos dont l'usage est autorisé sont publiés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
