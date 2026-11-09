# Plan de validation — Captcha

## Modèle de données
Défi, jeton, vérification serveur.

## Mise en œuvre attendue
Préférer champ piège et limites natives ; un captcha tiers exige une ouverture de la politique de contenu que le noyau ne délègue pas aux extensions.

## Tests à prévoir
1. Nominal : Vérifier que la protection choisie bloque un envoi automatisé.
2. Contrôle de refus : Aucun script de captcha n'est chargé sur les pages sans formulaire.
3. Invariant : Ne jamais affaiblir la Content-Security-Policy du site pour charger un script tiers.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
