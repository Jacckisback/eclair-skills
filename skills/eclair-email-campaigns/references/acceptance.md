# Plan de validation — Campagnes e-mail

## Modèle de données
Liste, segment, campagne, envoi, désinscription.

## Mise en œuvre attendue
Confier l'envoi à un service spécialisé, préparer les contenus depuis le site, définir segments, fréquence et désinscription.

## Tests à prévoir
1. Nominal : Envoyer une campagne de test à une liste interne.
2. Contrôle de refus : Une adresse désinscrite ne reçoit plus rien.
3. Invariant : Chaque e-mail contient un lien de désinscription fonctionnel ; aucune liste achetée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
