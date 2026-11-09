# Plan de validation — Intégrité des fichiers

## Modèle de données
Fichier, empreinte attendue, écart.

## Mise en œuvre attendue
Lancer le contrôle d'intégrité de la page Sécurité, expliquer chaque écart, restaurer les fichiers d'origine si besoin.

## Tests à prévoir
1. Nominal : Modifier un fichier sur une copie de test et constater l'alerte.
2. Contrôle de refus : Un fichier du noyau altéré n'est jamais déclaré conforme.
3. Invariant : Un écart inexpliqué est traité comme un incident, pas ignoré.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
