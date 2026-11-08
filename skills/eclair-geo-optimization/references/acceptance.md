# Plan de validation — GEO et agents IA

## Modèle de données
Contenu vérifiable, provenance, sémantique, llms.txt, Markdown, Schema.org.

## Implémentation attendue
Auditer structure, réponses factuelles, sources et cohérence du Markdown; contrôler robots IA sans sur-promesse.

## Tests à prévoir
1. Nominal : Tester version Markdown, citations structurées et robots.txt.
2. Contrôle de refus : Les faits affichés pour robots et humains restent cohérents et à jour.
3. Invariant : Ne pas confondre score GEO interne, citabilité et classement garanti.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
