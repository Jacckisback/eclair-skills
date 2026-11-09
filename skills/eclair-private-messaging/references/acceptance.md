# Plan de validation — Messagerie privée

## Modèle de données
Conversation, participants, message, signalement.

## Mise en œuvre attendue
Définir blocage, signalement, limites d'envoi et conservation ; aucune conversation dans une page en cache.

## Tests à prévoir
1. Nominal : Simuler échange, blocage et signalement.
2. Contrôle de refus : Un membre bloqué ne peut plus écrire à celui qui l'a bloqué.
3. Invariant : Un message n'est lisible que par ses participants.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
