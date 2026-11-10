# Plan de validation — Livraison et transport

## Modèle de données
Adresse validée, zone, transporteur, colis, poids, service, frais, tracking.

## Mise en œuvre attendue
Modéliser zones et incompatibilités; calculer devis côté serveur; prévoir split shipments et livraison partielle; anonymiser données d’expédition dans journaux.

## Tests à prévoir
1. Nominal : Tester zone hors service, poids limite, deux colis et statut perdu.
2. Contrôle de refus : Un numéro de suivi d’un client ne doit pas être visible depuis un autre compte.
3. Invariant : Adresse et suivi sont privés; aucune donnée personnelle dans cache public, logs détaillés ou URLs.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
