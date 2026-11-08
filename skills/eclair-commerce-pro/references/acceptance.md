# Plan de validation — Architecture Commerce Pro

## Modèle de données
Catalogue, panier, prix figés par ligne, commande, paiement, remboursement, stock, facture et journal de statut.

## Implémentation attendue
Dessiner une machine d’états commande/payment, séparer lecture publique et écritures privées, choisir stockage transactionnel, formaliser connecteur PSP; identifier les points non fournis par Éclair v2.

## Tests à prévoir
1. Nominal : Simuler achat, confirmation webhook, réessai, remboursement, stock et annulation.
2. Contrôle de refus : Même notification de paiement livrée deux fois => une seule transition de commande.
3. Invariant : Aucun paiement n’est déclaré réussi depuis la seule redirection navigateur; le serveur valide un événement PSP authentifié.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
