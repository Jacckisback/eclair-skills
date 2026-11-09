# Plan de validation — Déblocage progressif

## Modèle de données
Leçon, règle de déblocage, date ou condition, inscrit.

## Mise en œuvre attendue
Décrire les règles (date, délai après inscription, leçon précédente), les appliquer côté serveur à chaque demande.

## Tests à prévoir
1. Nominal : Simuler le passage du temps et la validation d'une leçon.
2. Contrôle de refus : Une adresse de leçon verrouillée devinée ne renvoie pas son contenu.
3. Invariant : Une leçon verrouillée n'est jamais envoyée au navigateur, même masquée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
