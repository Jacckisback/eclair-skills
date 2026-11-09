# Plan de validation — Commentaires

## Modèle de données
Commentaire, auteur, statut de modération, article, date.

## Mise en œuvre attendue
Définir file de modération, règles anti-spam, mentions légales et affichage en cache ; proposer en attendant un service externe ou une prise de contact.

## Tests à prévoir
1. Nominal : Simuler dépôt, modération, publication et suppression d'un commentaire.
2. Contrôle de refus : Un commentaire en attente ou refusé n'apparaît jamais dans une page en cache.
3. Invariant : Aucun commentaire n'est affiché sans modération ; aucune adresse e-mail n'est rendue publique.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
