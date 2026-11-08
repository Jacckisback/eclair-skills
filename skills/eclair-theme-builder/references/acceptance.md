# Plan de validation — Création de thème

## Modèle de données
theme.json, styles, assets, templates déclarés, licence et provenance.

## Implémentation attendue
Partir du thème exemple officiel, employer variables et gabarits supportés, tester preview puis ZIP, vérifier compatibilité version.

## Tests à prévoir
1. Nominal : Tester validateur thème, activation, prévisualisation et retour arrière.
2. Contrôle de refus : Un template défectueux ne rend pas le site inaccessible grâce au repli prévu.
3. Invariant : Ne jamais refaire SEO head et canonical ni toucher aux fichiers noyau.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
