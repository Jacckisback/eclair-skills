# Plan de validation — Rendez-vous et calendrier

## Modèle de données
Prestataire, service, durée, buffers, exceptions, événements et fuseaux.

## Implémentation attendue
Normaliser horaires en UTC, conserver fuseau d’affichage, bloquer créneaux d’indisponibilité, gérer resynchronisation externe.

## Tests à prévoir
1. Nominal : Tester DST, rendez-vous traversant minuit, événement supprimé.
2. Contrôle de refus : Un créneau bloqué manuellement n’est jamais proposé après resynchronisation.
3. Invariant : Une intégration externe nécessite OAuth/scopes minimaux et ne doit pas exposer les calendriers privés.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
