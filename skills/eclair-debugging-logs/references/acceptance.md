# Plan de validation — Diagnostic et journaux

## Modèle de données
Symptôme, journal serveur, journal du site, hypothèse, correction.

## Mise en œuvre attendue
Reproduire, lire les journaux du serveur et du site, isoler la fonction en cause en la désactivant, corriger puis vérifier.

## Tests à prévoir
1. Nominal : Provoquer une erreur dans une extension de test et la localiser.
2. Contrôle de refus : Aucune trace technique n'apparaît dans une page publique.
3. Invariant : L'affichage des erreurs n'est jamais activé sur le site public.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
