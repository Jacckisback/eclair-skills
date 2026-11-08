# Plan de validation — Formulaires et mini-CRM

## Modèle de données
Formulaire, champ, consentement, contact, source, ticket et statut.

## Implémentation attendue
Définir finalité et durée de conservation par formulaire; valider données serveur; protéger spam; cloisonner fichiers et droit de lecture.

## Tests à prévoir
1. Nominal : Tester spam, pièce jointe, doublon et suppression RGPD.
2. Contrôle de refus : Un utilisateur sans droit ne peut pas exporter la base des contacts.
3. Invariant : Un formulaire public ne doit pas autoriser injection email ni faire apparaître les données dans le cache.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
