# Plan de validation — Accessibilité WCAG

## Modèle de données
Structure des titres, navigation clavier, focus, formulaires, médias, contrastes.

## Implémentation attendue
Réaliser audit clavier et lecteur d’écran, vérifier axe-core, contrastes, messages d’erreur et mouvement réduit.

## Tests à prévoir
1. Nominal : Tester parcours sans souris, erreurs de formulaire et zoom 200%.
2. Contrôle de refus : Un formulaire reste compréhensible sans couleur et depuis le clavier.
3. Invariant : Ne pas supprimer focus visible ou rendre une fonction dépendante uniquement de couleur ou geste.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
