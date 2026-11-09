# Plan de validation — Fils de réseaux sociaux

## Modèle de données
Publication, image, lien, date de récupération.

## Mise en œuvre attendue
Récupérer les publications par tâche planifiée côté serveur quand le réseau l'autorise, les rendre en HTML statique ; sinon simples liens vers les profils.

## Tests à prévoir
1. Nominal : Vérifier le rendu statique et la mise à jour par tâche.
2. Contrôle de refus : Si le réseau est indisponible, la dernière version valide reste affichée.
3. Invariant : Aucun widget tiers n'est chargé dans le navigateur des visiteurs.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
