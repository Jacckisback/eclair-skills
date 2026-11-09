# Plan de validation — Dons et associations

## Modèle de données
Cause, projet, montant, lien de don, reçu.

## Mise en œuvre attendue
Présenter mission et usage des fonds, relier les boutons de don à des liens du prestataire, renvoyer la gestion des reçus au prestataire ou à l'association.

## Tests à prévoir
1. Nominal : Faire un don en mode test et suivre le parcours complet.
2. Contrôle de refus : Un montant modifié dans la page ne change pas le montant encaissé.
3. Invariant : Aucune promesse d'avantage fiscal sans confirmation de l'association.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
