# Plan de validation — Types de contenu personnalisés

## Modèle de données
Fiche métier, champs, liste, adresse, statut.

## Mise en œuvre attendue
Choisir entre pages avec blocs dédiés et extension avec stockage propre et routes GET, fixer les adresses, prévoir liste et fiche.

## Tests à prévoir
1. Nominal : Créer un type de fiche par extension, avec liste et détail en GET, puis valider le paquet.
2. Contrôle de refus : Une fiche non publiée n'est servie ni en liste ni par son adresse directe.
3. Invariant : Ne jamais écrire dans les fichiers de contenus du noyau depuis une extension.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
