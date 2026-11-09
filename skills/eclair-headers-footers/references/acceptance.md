# Plan de validation — En-têtes et pieds de page

## Modèle de données
Logo, menu, coordonnées, liens légaux.

## Mise en œuvre attendue
Passer par un paquet de thème dans site/themes, respecter les variables du contrat de thème, garder lien d'évitement et liens légaux.

## Tests à prévoir
1. Nominal : Valider le thème et vérifier en-tête et pied de page sur toutes les pages types.
2. Contrôle de refus : Le thème refusé par le validateur n'est pas livré.
3. Invariant : Ne jamais générer soi-même balises SEO ou en-têtes déjà fournis par le noyau.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
