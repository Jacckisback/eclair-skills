# Plan de validation — Architecture Commerce Pro

## Modèle de données
Catalogue, panier, prix figés par ligne, commande, paiement, remboursement, stock, facture et journal de statut.

## Mise en œuvre attendue
Dessiner une machine d’états commande/payment, séparer lecture publique et écritures privées, choisir stockage transactionnel, formaliser connecteur PSP; identifier les points non fournis par Éclair v2.

## Tests à prévoir
1. Nominal : Simuler achat, confirmation webhook, réessai, remboursement, stock et annulation.
2. Contrôle de refus : Même notification de paiement livrée deux fois => une seule transition de commande.
3. Invariant : Aucun paiement n’est déclaré réussi depuis la seule redirection navigateur; le serveur valide un événement PSP authentifié.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
