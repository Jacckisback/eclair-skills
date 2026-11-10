# Plan de validation — Webhooks entrants et sortants

## Modèle de données
Source, secret, événement, signature, horodatage, ID unique, tentative, résultat.

## Mise en œuvre attendue
Spécifier contrat, vérifier signature sur octets bruts, anti-rejeu et file durable; documenter retries/dlq et endpoint POST privé.

## Tests à prévoir
1. Nominal : Tester envoi double, retard, ordre inversé et secret changé.
2. Contrôle de refus : Deux tentatives du même webhook ne déclenchent qu’une seule mutation métier.
3. Invariant : Ne jamais publier un webhook avec secret dans URL ni traiter événement financier non signé.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
