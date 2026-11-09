# Plan de validation — Sauvegardes et restauration

## Modèle de données
Archive de sauvegarde, date, destination, test de restauration.

## Mise en œuvre attendue
Activer la sauvegarde téléchargeable ou vers le stockage distant prévu par le noyau, fixer la fréquence, restaurer sur une copie pour vérifier.

## Tests à prévoir
1. Nominal : Restaurer la dernière sauvegarde sur une installation de test et comparer.
2. Contrôle de refus : Une archive modifiée ou piégée est refusée à la restauration.
3. Invariant : Une sauvegarde contient des données personnelles : elle est stockée chiffrée ou en lieu sûr, jamais dans un dossier public.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
