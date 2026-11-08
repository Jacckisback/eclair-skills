---
name: eclair-security-audit
description: Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security.
---

# Éclair Security Audit — revue avant activation

## Périmètre
1. Établir la version du noyau, provenance de l'extension, fichiers exécutables et permissions réclamées.
2. Exiger le contrat `extension.json` conforme et des empreintes SHA-256 pour les fichiers ; vérifier symlinks, chemins traversants, scripts imprévus, ZIP bombs, tailles, méthodes et routes réservées.
3. Contrôler séparément `right` natif de route admin et autorisations métier sur les objets ; un droit `content` n'autorise pas à lire la commande d'un autre client.
4. Tester CSRF, rate limiting, session fixation, accès direct aux fichiers, XSS dans HTML renvoyé, injection SQL, SSRF des URLs externes, et gestion des secrets.
5. Pages publiques avec `cache:true` : absence de données personnelles et de variantes par utilisateur. Pages admin : headers, authentification et refus par défaut.
6. Pour un checkout : webhook signé avec vérification serveur, idempotence, montants, devise, TVA et transitions d'état transactionnelles avant livraison.
7. Pour des événements métiers : rappeler que v2 n'intègre pas de bus/outbox standard ; projet séparé avec tests de panne et aucune promesse d'exactly-once pour des effets distants.
8. Ne jamais exécuter des modules non audités avec la confiance du processus PHP.

## Preuves minimales
`php tools/validate.php chemin/extension --json`, `php tests/run.php`, `php tools/measure.php --check` et scénarios négatifs HTTP sur une installation de test. Aucun rapport de sécurité n'est une certification automatique.

## Livrables
Liste de risques classés, démonstrations reproductibles, correctifs, limites restantes et décision explicite Go/No-Go.

## V1.0 — Tests de l'identité
Auditer le prototype `member-directory` : aucun compte membre dans `data/users.php`, mot de passe jamais restitué, statut `pending` par défaut, rôles `admin/editor` interdits, epoch de révocation, contrôle objet propre/autrui, cookie `__Host-` HTTPS. Les tests locaux ne valent pas audit en production.

## Éclair 2.0 — prototype v1.1 (experimental)
Le prototype v1.1 a une limitation `RateLimit::attempt` avant hash, une séparation stricte membres/admin et des jetons de session 256 bits. Évaluer la sécurité des `Origin`, de TLS derrière reverse proxy, CSRF, IDOR, énumération de comptes, fuites d’informations et concurrence. Ne pas confondre tests isolés et audit en production.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
