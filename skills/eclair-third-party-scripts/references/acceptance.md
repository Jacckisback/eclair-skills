# Plan de validation — Scripts tiers

## Modèle de données
Script, finalité, poids, domaine, consentement requis.

## Mise en œuvre attendue
Inventorier chaque demande de script, chercher une alternative sans script, documenter le blocage par la politique de contenu native quand il existe.

## Tests à prévoir
1. Nominal : Mesurer poids et requêtes avant et après chaque ajout accepté.
2. Contrôle de refus : Un script d'un domaine non autorisé ne s'exécute pas.
3. Invariant : Aucun script n'est injecté en contournant la Content-Security-Policy.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
