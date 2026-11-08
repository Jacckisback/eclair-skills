# Plan de validation — Réservations métier

## Modèle de données
Ressource, plage, capacité, fuseau, état et réservation.

## Implémentation attendue
Définir règles de disponibilité et annulation, verrouiller les créneaux transactionnellement, distinguer option et réservation ferme.

## Tests à prévoir
1. Nominal : Tester clients simultanés, changements d’heure et annulation.
2. Contrôle de refus : Dernière place réservée simultanément => une seule confirmation.
3. Invariant : Aucun calendrier GET en cache ne remplace la validation transactionnelle de disponibilité.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
