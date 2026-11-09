# Plan de validation — Pages d'erreur

## Modèle de données
Page d'erreur, liens utiles, journal des adresses introuvables.

## Mise en œuvre attendue
Composer une page 404 utile dans le thème de site, proposer accueil et pages clés, traiter les 404 fréquentes par redirection.

## Tests à prévoir
1. Nominal : Demander une adresse inexistante et vérifier statut 404 et contenu.
2. Contrôle de refus : Une page introuvable ne répond jamais avec un statut 200.
3. Invariant : La page d'erreur n'affiche aucune trace technique.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
