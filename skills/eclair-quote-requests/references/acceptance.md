# Plan de validation — Demandes de devis

## Modèle de données
Demande, prestation, budget, délai, coordonnées.

## Mise en œuvre attendue
Commencer avec le formulaire de contact natif et des questions guidées dans la page ; concevoir le formulaire structuré pour plus tard.

## Tests à prévoir
1. Nominal : Envoyer une demande type et vérifier sa réception complète.
2. Contrôle de refus : Une demande sans coordonnées valides est refusée avec un message clair.
3. Invariant : Seules les données utiles au devis sont demandées.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
