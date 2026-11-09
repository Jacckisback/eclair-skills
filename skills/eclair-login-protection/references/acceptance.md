# Plan de validation — Protection de la connexion

## Modèle de données
Tentatives, limites par réseau et par compte, adresse d'administration.

## Mise en œuvre attendue
Contrôler les limites de tentatives natives, l'adresse d'administration, les sessions actives et les mots de passe provisoires.

## Tests à prévoir
1. Nominal : Simuler des échecs répétés et constater le blocage.
2. Contrôle de refus : L'appareil habituel du propriétaire n'est pas bloqué par les essais d'un tiers.
3. Invariant : Aucune limite native n'est relâchée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
