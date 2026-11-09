# Plan de validation — Services d'e-mailing

## Modèle de données
Liste, formulaire hébergé, clé d'API, synchronisation.

## Mise en œuvre attendue
Utiliser le formulaire hébergé du service ; ranger toute clé d'API dans les secrets de l'extension ; synchroniser par tâche si nécessaire.

## Tests à prévoir
1. Nominal : Inscrire une adresse de test et la retrouver dans le service.
2. Contrôle de refus : Une clé révoquée produit une erreur journalisée, pas une fuite.
3. Invariant : Aucune clé d'API dans le code, le dépôt ou une page publique.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
