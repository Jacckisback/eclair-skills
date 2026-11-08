# Plan de validation — Direction artistique Éclair

## Modèle de données
Positionnement, identité, typographie, couleurs, composants, photographies et contenu réel.

## Implémentation attendue
Définir univers tiré du métier, composer sections, ajuster CSS et tester thèmes avec du vrai contenu; privilégier site/themes et les blocs existants.

## Tests à prévoir
1. Nominal : Tester contraste, cohérence multi-page et versions mobile.
2. Contrôle de refus : La nouvelle apparence reste lisible sans JavaScript et respecte les liens existants.
3. Invariant : Ne jamais modifier app/theme/ ni casser le SEO, la CSP ou le chemin rapide.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
