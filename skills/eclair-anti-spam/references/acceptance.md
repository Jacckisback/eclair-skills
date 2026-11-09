# Plan de validation — Protection contre le spam

## Modèle de données
Message, jeton de formulaire, limite de fréquence.

## Mise en œuvre attendue
S'appuyer sur le jeton et les limites du formulaire natif, ajouter si besoin un champ piège, surveiller la boîte de réception.

## Tests à prévoir
1. Nominal : Envoyer un message légitime puis une rafale automatisée.
2. Contrôle de refus : Un envoi sans jeton valide est rejeté.
3. Invariant : Aucun service tiers ne reçoit les messages des visiteurs sans information préalable.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
