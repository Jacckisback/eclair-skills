# Plan de validation — Modération et signalements

## Modèle de données
Signalement, motif, élément visé, décision, modérateur, audit.

## Mise en œuvre attendue
Prévoir file de traitement, signalements abusifs, seuils/quotas, rollback et motifs; tracer décisions et restreindre pouvoirs par rôle.

## Tests à prévoir
1. Nominal : Tester modérateur sans droit global, utilisateur suspendu et appel.
2. Contrôle de refus : Un modérateur d’une catégorie ne peut pas voir les signalements privés d’une autre.
3. Invariant : Aucune suppression définitive automatique par signalement sans contrôle et preuves.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
