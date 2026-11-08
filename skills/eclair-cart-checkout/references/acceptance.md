# Plan de validation — Panier et tunnel de commande

## Modèle de données
Panier temporaire, session membre ou invité, lignes, promotions, frais, taxes, état de commande.

## Implémentation attendue
Séparer affichage et changement d’état; revalider chaque ligne sur le serveur; calculer les montants en unités monétaires entières; réserver le stock transactionnellement au bon moment.

## Tests à prévoir
1. Nominal : Tester modification simultanée de panier, expiration et changement de prix.
2. Contrôle de refus : Soumission double ou concurrente ne crée pas deux commandes payables pour la même clé.
3. Invariant : Aucune opération d’écriture publique avant route POST qualifiée, CSRF, quotas et droits vérifiés.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
