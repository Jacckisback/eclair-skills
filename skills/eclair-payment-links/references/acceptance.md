# Plan de validation — Liens de paiement

## Modèle de données
Produit ou variante, lien de paiement, prestataire.

## Mise en œuvre attendue
Créer le lien chez le prestataire, le coller dans la fiche ou la variante, tester en mode test, vérifier reçu et remboursement côté prestataire.

## Tests à prévoir
1. Nominal : Acheter en mode test et vérifier montant et reçu.
2. Contrôle de refus : Un lien vers un domaine non reconnu est refusé.
3. Invariant : Aucune donnée bancaire sur le site ; un lien ne mène qu'au domaine du prestataire.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
