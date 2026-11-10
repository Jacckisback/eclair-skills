# Plan de validation — Réservations métier

## Modèle de données
Ressource, plage, capacité, fuseau, état et réservation.

## Mise en œuvre attendue
Définir règles de disponibilité et annulation, verrouiller les créneaux transactionnellement, distinguer option et réservation ferme.

## Tests à prévoir
1. Nominal : Tester clients simultanés, changements d’heure et annulation.
2. Contrôle de refus : Dernière place réservée simultanément => une seule confirmation.
3. Invariant : Aucun calendrier GET en cache ne remplace la validation transactionnelle de disponibilité.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
