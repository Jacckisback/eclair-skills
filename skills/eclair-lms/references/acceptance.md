# Plan de validation — Architecture LMS

## Modèle de données
Cours, sections, leçons, prérequis, inscriptions, progrès, droits et ventes éventuelles.

## Implémentation attendue
Définir catalogues publics vs leçons privées; choisir un stockage de progression transactionnel; relier accès à l’identité membre validée; composer modules indépendants.

## Tests à prévoir
1. Nominal : Tester étudiant, professeur, administrateur et visiteur.
2. Contrôle de refus : Un élève inscrit ne peut pas lire le contenu privé d’un autre cours.
3. Invariant : Pas de promesse d’accès privé via une simple URL secrète ou un bloc caché.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
