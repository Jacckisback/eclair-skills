# Plan de validation — Champs personnalisés

## Modèle de données
Champ, type déclaré, valeur validée, bloc ou réglage porteur.

## Mise en œuvre attendue
Déclarer les champs dans le manifeste (types pris en charge par le noyau), laisser le noyau valider et stocker, rendre avec échappement.

## Tests à prévoir
1. Nominal : Déclarer un bloc avec champs texte, nombre et choix, puis vérifier validation et rendu.
2. Contrôle de refus : Une valeur hors format est refusée par le noyau et n'atteint jamais le rendu.
3. Invariant : Toute valeur affichée passe par e() ; aucun champ ne contient de secret.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
