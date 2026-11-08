# Plan de validation — Offres d’emploi

## Modèle de données
Offre, entreprise, statut, échéance, candidature et pièces jointes.

## Implémentation attendue
Construire filtres publics, expiration automatique, formulaires sécurisés et cycle de rétention des candidatures.

## Tests à prévoir
1. Nominal : Tester annonce expirée, spam et export candidat.
2. Contrôle de refus : Un recruteur ne peut pas lire une candidature destinée à une autre entreprise.
3. Invariant : CV et pièces jointes ne sont jamais placés dans un répertoire web accessible.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
