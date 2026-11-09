# Plan de validation — Inscription à la newsletter

## Modèle de données
Adresse e-mail, consentement, date, source.

## Mise en œuvre attendue
Utiliser une page d'inscription hébergée par le service d'e-mailing ou un lien, tant que le site ne peut pas recevoir d'inscription lui-même ; double confirmation.

## Tests à prévoir
1. Nominal : S'inscrire, confirmer, se désinscrire.
2. Contrôle de refus : Une inscription non confirmée ne reçoit aucun envoi.
3. Invariant : Aucune adresse n'est ajoutée à une liste sans consentement explicite et preuve.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
