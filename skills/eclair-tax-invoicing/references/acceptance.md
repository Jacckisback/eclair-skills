# Plan de validation — TVA et facturation

## Modèle de données
Pays de vente et livraison, localisation fiscale, taux en vigueur, facture, avoir, séquence.

## Implémentation attendue
Lister juridictions et types de clients; consulter règles à jour et conseil comptable; figer base taxable/taux au moment de la commande; préparer exports de factures et avoirs.

## Tests à prévoir
1. Nominal : Tester vente domestique, transfrontalière, remboursement et changement de taux.
2. Contrôle de refus : Facture émise puis annulée ne doit pas être effacée ou renumérotée silencieusement.
3. Invariant : Ne jamais appliquer un taux TVA universel ou prétendre assurer conformité fiscale sans validation locale.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
