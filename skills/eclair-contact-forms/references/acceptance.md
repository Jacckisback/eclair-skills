# Plan de validation — Formulaire de contact

## Modèle de données
Message, nom, e-mail, sujet, date, statut de lecture.

## Mise en œuvre attendue
Placer le bloc contact natif, régler le destinataire, tester l'envoi et la réception, afficher la mention d'information.

## Tests à prévoir
1. Nominal : Envoyer un message réel et le retrouver dans l'administration et par e-mail.
2. Contrôle de refus : Des envois répétés en rafale sont limités par le noyau.
3. Invariant : Les messages ne sont visibles que par les comptes ayant le droit Messages.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
