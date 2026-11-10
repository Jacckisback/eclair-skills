# Plan de validation — Direction artistique Éclair

## Modèle de données
Positionnement, identité, typographie, couleurs, composants, photographies et contenu réel.

## Mise en œuvre attendue
Définir univers tiré du métier, composer sections, ajuster CSS et tester thèmes avec du vrai contenu; privilégier site/themes et les blocs existants.

## Tests à prévoir
1. Nominal : Tester contraste, cohérence multi-page et versions mobile.
2. Contrôle de refus : La nouvelle apparence reste lisible sans JavaScript et respecte les liens existants.
3. Invariant : Ne jamais modifier app/theme/ ni casser le SEO, la CSP ou le chemin rapide.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
