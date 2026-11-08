# Plan de validation — Webhooks entrants et sortants

## Modèle de données
Source, secret, événement, signature, horodatage, ID unique, tentative, résultat.

## Implémentation attendue
Spécifier contrat, vérifier signature sur octets bruts, anti-rejeu et file durable; documenter retries/dlq et endpoint POST privé.

## Tests à prévoir
1. Nominal : Tester envoi double, retard, ordre inversé et secret changé.
2. Contrôle de refus : Deux tentatives du même webhook ne déclenchent qu’une seule mutation métier.
3. Invariant : Ne jamais publier un webhook avec secret dans URL ni traiter événement financier non signé.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
