# Plan de validation — GEO et agents IA

## Modèle de données
Contenu vérifiable, provenance, sémantique, llms.txt, Markdown, Schema.org.

## Mise en œuvre attendue
Auditer structure, réponses factuelles, sources et cohérence du Markdown; contrôler robots IA sans sur-promesse.

## Tests à prévoir
1. Nominal : Tester version Markdown, citations structurées et robots.txt.
2. Contrôle de refus : Les faits affichés pour robots et humains restent cohérents et à jour.
3. Invariant : Ne pas confondre score GEO interne, citabilité et classement garanti.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
