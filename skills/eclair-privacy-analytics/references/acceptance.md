# Plan de validation — Mesure d'audience respectueuse

## Modèle de données
Page vue, source, période, agrégats.

## Mise en œuvre attendue
Préférer les journaux du serveur ou un outil sans cookie auto-hébergé ; un script tiers dépend de la politique de contenu native.

## Tests à prévoir
1. Nominal : Comparer les pages vues mesurées à un parcours de test.
2. Contrôle de refus : Aucun cookie n'est déposé par la mesure.
3. Invariant : Aucune adresse IP complète ni identifiant de visiteur n'est conservé.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
