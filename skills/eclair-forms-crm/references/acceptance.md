# Plan de validation — Formulaires et mini-CRM

## Modèle de données
Formulaire, champ, consentement, contact, source, ticket et statut.

## Mise en œuvre attendue
Définir finalité et durée de conservation par formulaire; valider données serveur; protéger spam; cloisonner fichiers et droit de lecture.

## Tests à prévoir
1. Nominal : Tester spam, pièce jointe, doublon et suppression RGPD.
2. Contrôle de refus : Un utilisateur sans droit ne peut pas exporter la base des contacts.
3. Invariant : Un formulaire public ne doit pas autoriser injection email ni faire apparaître les données dans le cache.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
