# Plan de validation — Cartes et plans d'accès

## Modèle de données
Adresse, coordonnées, image de carte, lien d'itinéraire.

## Mise en œuvre attendue
Préférer une image de carte statique avec lien vers l'itinéraire ; une carte interactive tierce dépend de la politique de contenu native.

## Tests à prévoir
1. Nominal : Vérifier image, texte alternatif et lien d'itinéraire sur mobile.
2. Contrôle de refus : Aucune requête vers un service de cartes au chargement de la page.
3. Invariant : Aucune carte tierce chargée avant une action du visiteur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
