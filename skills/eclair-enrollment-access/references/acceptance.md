# Plan de validation — Inscriptions aux cours

## Modèle de données
Membre, cours, inscription, état, origine, date et révocation.

## Mise en œuvre attendue
Créer inscription idempotente; traiter droits par objet; distinguer inscription gratuite/payant; révoquer après remboursement selon règle explicite.

## Tests à prévoir
1. Nominal : Tester double achat, remboursement, suspension du compte.
2. Contrôle de refus : Un membre radié ne peut plus accéder aux leçons auparavant autorisées.
3. Invariant : Jamais d’inscription automatique sur une simple URL de retour prestataire de paiement.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
