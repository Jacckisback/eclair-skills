# Plan de validation — Flux éditorial

## Modèle de données
Brouillon, auteur, relecteur, date prévue, statut, entrée de planning.

## Mise en œuvre attendue
Fixer qui rédige et qui publie selon les droits natifs, utiliser le planning éditorial et les brouillons, garder une relecture humaine avant toute mise en ligne.

## Tests à prévoir
1. Nominal : Faire passer un contenu de l'idée au brouillon puis à la publication par une personne habilitée.
2. Contrôle de refus : Un compte limité aux contenus ne peut ni changer les réglages ni publier à la place d'un autre rôle.
3. Invariant : Un agent ou un rédacteur sans droit de publication ne met rien en ligne.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
