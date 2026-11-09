---
name: eclair-live-classes
description: "Announce and organise live video classes. Use on Éclair CMS 2.x when the user wants to: annoncer et organiser des classes en visioconférence. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Classes en direct — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **annoncer et organiser des classes en visioconférence**. La **partie publique en lecture est réalisable aujourd'hui** ; les écritures par les visiteurs demandent davantage que le contrat actuel. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Intégrations Zoom des LMS. Famille : LMS.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Séance, date, fuseau, lien de connexion, inscrits**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Publier le calendrier des séances en GET, envoyer le lien de connexion par le service de visioconférence ou par e-mail, pas sur une page publique. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** La lecture publique (GET, cacheable) est réalisable aujourd'hui. Toute écriture par un visiteur exige une route POST publique que le noyau 2.0 n'ouvre pas aux extensions (PR #19 en brouillon, non fusionnée) : ne pas la simuler.
7. **Invariant de sécurité :** Le lien d'une séance payante ou privée n'est jamais publié. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Vérifier l'affichage des dates dans deux fuseaux » et le test de refus « Une séance passée n'est plus proposée à l'inscription ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet en lecture seule (routes GET) validé, et plan écrit pour la partie en écriture, clairement marquée non livrée.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Vérifier l'affichage des dates dans deux fuseaux.
- Une séance passée n'est plus proposée à l'inscription.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `public-read-only-prototype-possible`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
