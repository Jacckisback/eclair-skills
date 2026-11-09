# Plan de validation — Groupes

## Modèle de données
Groupe, visibilité, membres, rôles.

## Mise en œuvre attendue
Définir création, adhésion, rôles et visibilité ; appliquer les droits à chaque lecture.

## Tests à prévoir
1. Nominal : Simuler création, demande d'adhésion et exclusion.
2. Contrôle de refus : Un non-membre ne lit aucun contenu d'un groupe privé.
3. Invariant : Le contenu d'un groupe privé n'apparaît ni en recherche ni en cache public.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
