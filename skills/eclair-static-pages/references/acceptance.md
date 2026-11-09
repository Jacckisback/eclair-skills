# Plan de validation — Pages du site

## Modèle de données
Page, adresse, blocs, page parente, statut, entrée de menu.

## Mise en œuvre attendue
Lister les pages nécessaires, fixer les adresses avant rédaction, composer chaque page en blocs et relier les pages entre elles.

## Tests à prévoir
1. Nominal : Créer l'arborescence complète et contrôler chaque adresse, le menu et le fil d'Ariane.
2. Contrôle de refus : Une page renommée répond par une redirection 301 unique, jamais par une erreur 404.
3. Invariant : Ne jamais changer l'adresse d'une page publiée sans redirection vérifiée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
