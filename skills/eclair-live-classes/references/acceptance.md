# Plan de validation — Classes en direct

## Modèle de données
Séance, date, fuseau, lien de connexion, inscrits.

## Mise en œuvre attendue
Publier le calendrier des séances en GET, envoyer le lien de connexion par le service de visioconférence ou par e-mail, pas sur une page publique.

## Tests à prévoir
1. Nominal : Vérifier l'affichage des dates dans deux fuseaux.
2. Contrôle de refus : Une séance passée n'est plus proposée à l'inscription.
3. Invariant : Le lien d'une séance payante ou privée n'est jamais publié.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
