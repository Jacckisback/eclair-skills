# Plan de validation — TVA et facturation

## Modèle de données
Pays de vente et livraison, localisation fiscale, taux en vigueur, facture, avoir, séquence.

## Mise en œuvre attendue
Lister juridictions et types de clients; consulter règles à jour et conseil comptable; figer base taxable/taux au moment de la commande; préparer exports de factures et avoirs.

## Tests à prévoir
1. Nominal : Tester vente domestique, transfrontalière, remboursement et changement de taux.
2. Contrôle de refus : Facture émise puis annulée ne doit pas être effacée ou renumérotée silencieusement.
3. Invariant : Ne jamais appliquer un taux TVA universel ou prétendre assurer conformité fiscale sans validation locale.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
