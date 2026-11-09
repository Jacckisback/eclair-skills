# Plan de validation — Formulaires de paiement

## Modèle de données
Prestation, montant, lien de paiement du prestataire.

## Mise en œuvre attendue
Créer le lien chez le prestataire de paiement, l'afficher sur une page claire avec conditions, ne rien stocker sur le site.

## Tests à prévoir
1. Nominal : Payer en mode test et vérifier reçu et page de retour.
2. Contrôle de refus : Un montant modifié côté navigateur n'a aucun effet sur le montant encaissé.
3. Invariant : Aucune donnée bancaire ne transite ni n'est stockée sur le site.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
