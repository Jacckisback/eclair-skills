# Plan de validation — Inscriptions aux cours

## Modèle de données
Membre, cours, inscription, état, origine, date et révocation.

## Implémentation attendue
Créer inscription idempotente; traiter droits par objet; distinguer inscription gratuite/payant; révoquer après remboursement selon règle explicite.

## Tests à prévoir
1. Nominal : Tester double achat, remboursement, suspension du compte.
2. Contrôle de refus : Un membre radié ne peut plus accéder aux leçons auparavant autorisées.
3. Invariant : Jamais d’inscription automatique sur une simple URL de retour prestataire de paiement.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
