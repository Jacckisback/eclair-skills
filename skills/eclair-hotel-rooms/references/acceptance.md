# Plan de validation — Hébergements et chambres

## Modèle de données
Chambre, capacité, équipements, tarifs indicatifs, lien de réservation.

## Mise en œuvre attendue
Présenter chaque hébergement en fiche, renvoyer vers le moteur de réservation existant ou la demande par formulaire.

## Tests à prévoir
1. Nominal : Parcourir fiches et lien de réservation sur mobile.
2. Contrôle de refus : Une chambre retirée n'est plus proposée.
3. Invariant : Aucune disponibilité ni tarif affichés comme garantis s'ils ne viennent pas du système de réservation.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
