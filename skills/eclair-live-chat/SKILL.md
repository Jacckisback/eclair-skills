---
name: eclair-live-chat
description: "Offer instant contact without a heavy widget. Use on Éclair CMS 2.x when the user wants to: proposer un contact immédiat sans widget lourd. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Discussion en direct — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **proposer un contact immédiat sans widget lourd**. Cette fonction est **en partie bloquée par le contrat du noyau** : le skill livre ce qui est natif et documente l'écart. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Tidio, Crisp, tawk.to. Famille : Intégrations et automatisations.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Canal, horaires, lien de conversation**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Préférer un lien vers une messagerie (WhatsApp, e-mail, téléphone) avec horaires ; un widget tiers dépend de la politique de contenu native. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Une partie dépend d'un point d'accroche absent du contrat 2.0 (types de contenu, contribution SEO ou JSON-LD, politique de contenu par fonction, filtre de rendu). Livrer la partie native et documenter précisément l'écart, sans contournement.
7. **Invariant de sécurité :** Aucun widget ne charge de traceur avant une action du visiteur. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Ouvrir le canal depuis mobile et ordinateur » et le test de refus « Hors horaires, le site l'annonce au lieu de promettre une réponse immédiate ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet ou réglages pour la partie native, et note d'écart précise pour la partie bloquée.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Ouvrir le canal depuis mobile et ordinateur.
- Hors horaires, le site l'annonce au lieu de promettre une réponse immédiate.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `partly-blocked-by-core-contract`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
