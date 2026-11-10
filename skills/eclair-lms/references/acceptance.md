# Plan de validation — Architecture LMS

## Modèle de données
Cours, sections, leçons, prérequis, inscriptions, progrès, droits et ventes éventuelles.

## Mise en œuvre attendue
Définir catalogues publics vs leçons privées; choisir un stockage de progression transactionnel; relier accès à l’identité membre validée; composer modules indépendants.

## Tests à prévoir
1. Nominal : Tester étudiant, professeur, administrateur et visiteur.
2. Contrôle de refus : Un élève inscrit ne peut pas lire le contenu privé d’un autre cours.
3. Invariant : Pas de promesse d’accès privé via une simple URL secrète ou un bloc caché.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
