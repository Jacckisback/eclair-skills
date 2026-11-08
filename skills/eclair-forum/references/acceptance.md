# Plan de validation — Architecture Forum

## Modèle de données
Espace, catégorie, sujet, message, auteur, rôle, signalement, verrouillage.

## Implémentation attendue
Séparer sujets indexables et privés; prévoir pagination stable, permissions objet, quotats et modération; préparer moteur de recherche borné.

## Tests à prévoir
1. Nominal : Tester visiteur, membre, modérateur et compte suspendu.
2. Contrôle de refus : Sujet privé inexistant pour un membre non autorisé y compris via recherche.
3. Invariant : Aucune écriture anonyme sans anti-spam, CSRF et limitation de débit; jamais de HTML arbitraire exécuté.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
