# Plan de validation — Profils de communauté

## Modèle de données
Pseudo unique, avatar, préférences de visibilité, réputation et rôles.

## Implémentation attendue
Distinguer ID interne et pseudo; imposer limites et modération avatar; exposer uniquement champs consentis; gérer renommages et redirections sûres.

## Tests à prévoir
1. Nominal : Tester collision de pseudonymes et suppression de compte.
2. Contrôle de refus : Un visiteur ne peut pas inférer un email par un message d’erreur ou une API de profil.
3. Invariant : Email, session, IP, adresse et informations de récupération restent privés.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
