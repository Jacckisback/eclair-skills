# Plan de validation — Architecture Forum

## Modèle de données
Espace, catégorie, sujet, message, auteur, rôle, signalement, verrouillage.

## Mise en œuvre attendue
Séparer sujets indexables et privés; prévoir pagination stable, permissions objet, quotats et modération; préparer moteur de recherche borné.

## Tests à prévoir
1. Nominal : Tester visiteur, membre, modérateur et compte suspendu.
2. Contrôle de refus : Sujet privé inexistant pour un membre non autorisé y compris via recherche.
3. Invariant : Aucune écriture anonyme sans anti-spam, CSRF et limitation de débit; jamais de HTML arbitraire exécuté.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
