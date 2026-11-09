# Plan de validation — Équipe

## Modèle de données
Personne, fonction, photo, courte biographie.

## Mise en œuvre attendue
Utiliser le bloc équipe natif avec photos homogènes et textes fournis par les personnes.

## Tests à prévoir
1. Nominal : Afficher l'équipe sur mobile avec textes alternatifs corrects.
2. Contrôle de refus : Une personne retirée disparaît aussi des pages en cache.
3. Invariant : Aucune photo ou information publiée sans l'accord de la personne.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
