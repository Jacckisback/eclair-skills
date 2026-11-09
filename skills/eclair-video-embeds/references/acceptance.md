# Plan de validation — Vidéos

## Modèle de données
Vidéo, source, image d'aperçu, sous-titres.

## Mise en œuvre attendue
Utiliser le bloc vidéo natif, préférer une façade cliquable pour les plateformes tierces, fournir sous-titres ou transcription.

## Tests à prévoir
1. Nominal : Vérifier qu'aucune requête tierce ne part avant le clic.
2. Contrôle de refus : Une adresse vidéo d'un domaine non autorisé est refusée.
3. Invariant : Aucun lecteur tiers n'est chargé avant le clic du visiteur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
