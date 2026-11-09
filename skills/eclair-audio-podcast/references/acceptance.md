# Plan de validation — Audio et podcast

## Modèle de données
Épisode, fichier audio, durée, notes, flux.

## Mise en œuvre attendue
Créer une page par épisode avec lecteur HTML natif, générer le flux de podcast en GET et héberger les fichiers lourds hors du site si nécessaire.

## Tests à prévoir
1. Nominal : Valider le flux avec un validateur de podcast et lire un épisode sur mobile.
2. Contrôle de refus : Un épisode en brouillon est absent du flux.
3. Invariant : Le flux ne référence que des épisodes publiés et des fichiers publics.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
