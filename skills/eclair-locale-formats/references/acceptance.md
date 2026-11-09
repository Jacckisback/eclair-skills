# Plan de validation — Formats régionaux

## Modèle de données
Langue, pays, devise, fuseau horaire.

## Mise en œuvre attendue
Centraliser le formatage côté serveur, ne jamais écrire un format en dur dans les gabarits.

## Tests à prévoir
1. Nominal : Comparer une date et un prix en français, anglais et allemand.
2. Contrôle de refus : Une devise inconnue n'est pas affichée avec un symbole par défaut trompeur.
3. Invariant : Un prix affiché correspond toujours à la devise réellement facturée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
