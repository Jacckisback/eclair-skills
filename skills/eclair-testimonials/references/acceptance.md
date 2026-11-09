# Plan de validation — Témoignages et avis

## Modèle de données
Témoignage, auteur, date, autorisation.

## Mise en œuvre attendue
Recueillir les témoignages réels avec autorisation écrite, les présenter en citations, indiquer la source.

## Tests à prévoir
1. Nominal : Vérifier que chaque témoignage publié a une autorisation consignée.
2. Contrôle de refus : Un avis sans source vérifiable n'est pas publié.
3. Invariant : Aucun avis inventé, modifié ou sélectionné de façon trompeuse.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
