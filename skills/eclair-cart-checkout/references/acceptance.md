# Plan de validation — Panier et tunnel de commande

## Modèle de données
Panier temporaire, session membre ou invité, lignes, promotions, frais, taxes, état de commande.

## Mise en œuvre attendue
Séparer affichage et changement d’état; revalider chaque ligne sur le serveur; calculer les montants en unités monétaires entières; réserver le stock transactionnellement au bon moment.

## Tests à prévoir
1. Nominal : Tester modification simultanée de panier, expiration et changement de prix.
2. Contrôle de refus : Soumission double ou concurrente ne crée pas deux commandes payables pour la même clé.
3. Invariant : Aucune opération d’écriture publique avant route POST qualifiée, CSRF, quotas et droits vérifiés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
