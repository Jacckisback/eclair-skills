# Plan de validation — Référencement local

## Modèle de données
Nom, adresse, téléphone, horaires, zone desservie.

## Mise en œuvre attendue
Renseigner les coordonnées exactes dans les réglages, vérifier le balisage d'entreprise locale produit par le noyau, aligner fiche d'établissement et site.

## Tests à prévoir
1. Nominal : Comparer coordonnées du site, du balisage et de la fiche d'établissement.
2. Contrôle de refus : Des horaires non confirmés ne sont pas publiés.
3. Invariant : Aucune adresse, avis ou zone d'intervention inventés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
