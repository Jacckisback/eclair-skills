---
name: eclair-email-automation
description: "Send reliable confirmations and reminders (transactional email). Use on Éclair CMS 2.x when the user wants to: envoyer confirmations et relances fiables. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Emails transactionnels — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **envoyer confirmations et relances fiables**. Cette fonction **exige des capacités absentes du noyau 2.0** : le skill livre conception, maquette sûre et tests, pas une mise en production. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** WP Mail SMTP, e-mails transactionnels. Famille : Intégrations et automatisations.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Template, langue, consentement, destinataire, domaine, événement, livraison**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Préparer modèles texte/HTML, DKIM/SPF/DMARC et délivrabilité; distinguer transactionnel et marketing, journal sans secrets, désabonnement requis. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Les tâches natives existent (minimum 3 600 secondes). Les webhooks entrants et interactions membres requièrent des routes POST qualifiées, une validation de signature et, pour les effets métiers, une outbox idempotente.
7. **Invariant de sécurité :** Ne pas envoyer token de récupération par URL non vérifiée; jamais de spam sans consentement. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Tester erreur SMTP, erreur d’adresse, reprise et expiration de token » et le test de refus « Un échec SMTP ne marque pas un email comme livré ni ne bloque un compte définitivement ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Dossier de conception, maquette GET sûre si utile, tests bloquants et demande d'évolution du noyau ; **pas de paquet de production**.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Tester erreur SMTP, erreur d’adresse, reprise et expiration de token.
- Un échec SMTP ne marque pas un email comme livré ni ne bloque un compte définitivement.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
