# Plan de validation — Médias pédagogiques

## Modèle de données
Leçon, média, transcription, fichiers téléchargeables, droits et durée.

## Implémentation attendue
Préparer médias et sous-titres accessibles; prévoir distribution avec autorisation côté serveur ou URL signée courte; séparer CDN public et contenu réservé.

## Tests à prévoir
1. Nominal : Tester média périmé, accès sans inscription et mobile.
2. Contrôle de refus : Une URL de document privé copiée dans un autre navigateur est refusée ou expire.
3. Invariant : Masquer un lien dans HTML n’est pas une protection; ne pas placer le média privé dans /media public.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
