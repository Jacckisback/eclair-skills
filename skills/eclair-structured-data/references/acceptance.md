# Plan de validation — Données structurées

## Modèle de données
WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList.

## Implémentation attendue
Inspecter JSON-LD natif avant d’ajouter un type; éviter duplication; aligner chaque champ avec les données visibles et les consignes des moteurs.

## Tests à prévoir
1. Nominal : Tester JSON valide, canonical, identifiants et contenu affiché.
2. Contrôle de refus : Aucun prix/avis/product inventé ou absent de la page ne figure en JSON-LD.
3. Invariant : Éclair v2 n’expose pas encore toutes les contributions JSON-LD aux extensions; proposer RFC plutôt qu’injection opaque.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
