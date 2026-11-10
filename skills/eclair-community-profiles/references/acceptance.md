# Plan de validation — Profils de communauté

## Modèle de données
Pseudo unique, avatar, préférences de visibilité, réputation et rôles.

## Mise en œuvre attendue
Distinguer ID interne et pseudo; imposer limites et modération avatar; exposer uniquement champs consentis; gérer renommages et redirections sûres.

## Tests à prévoir
1. Nominal : Tester collision de pseudonymes et suppression de compte.
2. Contrôle de refus : Un visiteur ne peut pas inférer un email par un message d’erreur ou une API de profil.
3. Invariant : Email, session, IP, adresse et informations de récupération restent privés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
