# Plan de validation — Médias pédagogiques

## Modèle de données
Leçon, média, transcription, fichiers téléchargeables, droits et durée.

## Mise en œuvre attendue
Préparer médias et sous-titres accessibles; prévoir distribution avec autorisation côté serveur ou URL signée courte; séparer CDN public et contenu réservé.

## Tests à prévoir
1. Nominal : Tester média périmé, accès sans inscription et mobile.
2. Contrôle de refus : Une URL de document privé copiée dans un autre navigateur est refusée ou expire.
3. Invariant : Masquer un lien dans HTML n’est pas une protection; ne pas placer le média privé dans /media public.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
