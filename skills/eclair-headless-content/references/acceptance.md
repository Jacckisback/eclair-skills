# Plan de validation — Contenu pour applications et IA

## Modèle de données
Version Markdown, llms.txt, flux, sitemap.

## Mise en œuvre attendue
S'appuyer sur les sorties natives lisibles par machine, documenter leur format et leur fraîcheur pour l'application cliente.

## Tests à prévoir
1. Nominal : Lire une page en HTML et en Markdown et comparer.
2. Contrôle de refus : Un brouillon n'a pas de version Markdown accessible.
3. Invariant : Aucun contenu privé n'est exposé par ces sorties.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
