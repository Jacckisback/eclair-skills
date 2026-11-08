# Plan de validation — Livraison et transport

## Modèle de données
Adresse validée, zone, transporteur, colis, poids, service, frais, tracking.

## Implémentation attendue
Modéliser zones et incompatibilités; calculer devis côté serveur; prévoir split shipments et livraison partielle; anonymiser données d’expédition dans journaux.

## Tests à prévoir
1. Nominal : Tester zone hors service, poids limite, deux colis et statut perdu.
2. Contrôle de refus : Un numéro de suivi d’un client ne doit pas être visible depuis un autre compte.
3. Invariant : Adresse et suivi sont privés; aucune donnée personnelle dans cache public, logs détaillés ou URLs.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
