# Plan de validation — Discussion en direct

## Modèle de données
Canal, horaires, lien de conversation.

## Mise en œuvre attendue
Préférer un lien vers une messagerie (WhatsApp, e-mail, téléphone) avec horaires ; un widget tiers dépend de la politique de contenu native.

## Tests à prévoir
1. Nominal : Ouvrir le canal depuis mobile et ordinateur.
2. Contrôle de refus : Hors horaires, le site l'annonce au lieu de promettre une réponse immédiate.
3. Invariant : Aucun widget ne charge de traceur avant une action du visiteur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
