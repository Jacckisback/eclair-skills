# Plan de validation — Rendez-vous et calendrier

## Modèle de données
Prestataire, service, durée, buffers, exceptions, événements et fuseaux.

## Mise en œuvre attendue
Normaliser horaires en UTC, conserver fuseau d’affichage, bloquer créneaux d’indisponibilité, gérer resynchronisation externe.

## Tests à prévoir
1. Nominal : Tester DST, rendez-vous traversant minuit, événement supprimé.
2. Contrôle de refus : Un créneau bloqué manuellement n’est jamais proposé après resynchronisation.
3. Invariant : Une intégration externe nécessite OAuth/scopes minimaux et ne doit pas exposer les calendriers privés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
