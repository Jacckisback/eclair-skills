# Catalogue complet — Éclair Skills v2.0.0

Généré à partir de `catalog.json` et des en-têtes `SKILL.md`. **57 Agent Skills = 57 guides pour agents, pas 57 extensions PHP.** Cible : Éclair CMS 2.0.x, contrat `eclair-extension/1`.

*Generated from `catalog.json` and `SKILL.md` front matter. 57 Agent Skills are agent guides, not 57 PHP extensions.*

## Fondations (8)

Contrat natif v2, tests et sécurité.

| Skill | Description (EN) |
|---|---|
| [`eclair-architecture`](../skills/eclair-architecture/SKILL.md) | Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC. |
| [`eclair-extension-builder`](../skills/eclair-extension-builder/SKILL.md) | Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract. |
| [`eclair-storage`](../skills/eclair-storage/SKILL.md) | Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress. |
| [`eclair-auth-roles`](../skills/eclair-auth-roles/SKILL.md) | Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles. |
| [`eclair-routing`](../skills/eclair-routing/SKILL.md) | Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility. |
| [`eclair-cache-contract`](../skills/eclair-cache-contract/SKILL.md) | Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets. |
| [`eclair-security-audit`](../skills/eclair-security-audit/SKILL.md) | Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security. |
| [`eclair-test-suite`](../skills/eclair-test-suite/SKILL.md) | Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations. |

## Commerce Pro (10)

Boutique transactionnelle et paiement, conception avant déploiement.

| Skill | Description (EN) |
|---|---|
| [`eclair-commerce-pro`](../skills/eclair-commerce-pro/SKILL.md) | Use when a user wants to concevoir une boutique complète, du catalogue à la commande livrée on Éclair CMS 2.x; design a architecture commerce pro workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-product-catalog`](../skills/eclair-product-catalog/SKILL.md) | Use when a user wants to construire un catalogue public rapide et indexable on Éclair CMS 2.x; design a catalogue produits workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-product-variants`](../skills/eclair-product-variants/SKILL.md) | Use when a user wants to modéliser tailles, couleurs et configurations sans erreurs de prix on Éclair CMS 2.x; design a variantes et attributs workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-cart-checkout`](../skills/eclair-cart-checkout/SKILL.md) | Use when a user wants to concevoir une commande multi-lignes avec prix et stock cohérents on Éclair CMS 2.x; design a panier et tunnel de commande workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-orders-payments`](../skills/eclair-orders-payments/SKILL.md) | Use when a user wants to implémenter les états de commande et des prestataires psp on Éclair CMS 2.x; design a commandes et paiements workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-tax-invoicing`](../skills/eclair-tax-invoicing/SKILL.md) | Use when a user wants to construire les points de branchement fiscaux adaptés à la juridiction on Éclair CMS 2.x; design a tva et facturation workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-inventory`](../skills/eclair-inventory/SKILL.md) | Use when a user wants to synchroniser le stock réel entre produits, variantes et commandes on Éclair CMS 2.x; design a stocks et réservations workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-shipping`](../skills/eclair-shipping/SKILL.md) | Use when a user wants to gérer les zones, tarifs, suivis et états de livraison on Éclair CMS 2.x; design a livraison et transport workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-discounts`](../skills/eclair-discounts/SKILL.md) | Use when a user wants to créer remises et coupons cohérents et non cumulés par erreur on Éclair CMS 2.x; design a promotions et coupons workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-commerce-analytics`](../skills/eclair-commerce-analytics/SKILL.md) | Use when a user wants to suivre ventes et conversions sans exposer de données clients on Éclair CMS 2.x; design a mesure des ventes workflow with native extension compatibility, security and acceptance gates. |

## LMS (7)

Cours, inscriptions, progression, certifications.

| Skill | Description (EN) |
|---|---|
| [`eclair-lms`](../skills/eclair-lms/SKILL.md) | Use when a user wants to structurer une école en ligne modulaire on Éclair CMS 2.x; design a architecture lms workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-course-builder`](../skills/eclair-course-builder/SKILL.md) | Use when a user wants to composer cours, sections et leçons versionnés on Éclair CMS 2.x; design a création de parcours workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-lessons-media`](../skills/eclair-lessons-media/SKILL.md) | Use when a user wants to fournir vidéos et documents protégés pour cours on Éclair CMS 2.x; design a médias pédagogiques workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-enrollment-access`](../skills/eclair-enrollment-access/SKILL.md) | Use when a user wants to lier achat ou validation à une inscription et à ses autorisations on Éclair CMS 2.x; design a inscriptions aux cours workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-progress`](../skills/eclair-progress/SKILL.md) | Use when a user wants to mesurer des acquis sans pertes ni mises à jour incohérentes on Éclair CMS 2.x; design a suivi de progression workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-quizzes-certificates`](../skills/eclair-quizzes-certificates/SKILL.md) | Use when a user wants to créer évaluations, seuils de réussite et certificats contrôlés on Éclair CMS 2.x; design a quiz et attestations workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-lms-analytics`](../skills/eclair-lms-analytics/SKILL.md) | Use when a user wants to analyser complétion et engagement sans surveillance abusive on Éclair CMS 2.x; design a tableau de bord pédagogique workflow with native extension compatibility, security and acceptance gates. |

## Forum et communauté (6)

Discussions, modération, profils et notifications.

| Skill | Description (EN) |
|---|---|
| [`eclair-forum`](../skills/eclair-forum/SKILL.md) | Use when a user wants to concevoir des discussions publiques et privées avec modération on Éclair CMS 2.x; design a architecture forum workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-discussions-topics`](../skills/eclair-discussions-topics/SKILL.md) | Use when a user wants to gérer création, édition et état des discussions on Éclair CMS 2.x; design a sujets et réponses workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-community-profiles`](../skills/eclair-community-profiles/SKILL.md) | Use when a user wants to proposer profils publics choisis séparés des données privées on Éclair CMS 2.x; design a profils de communauté workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-moderation`](../skills/eclair-moderation/SKILL.md) | Use when a user wants to construire outils de retrait, signalement et appel on Éclair CMS 2.x; design a modération et signalements workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-notifications`](../skills/eclair-notifications/SKILL.md) | Use when a user wants to informer sans spam ni fuite de données on Éclair CMS 2.x; design a notifications de communauté workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-community-search`](../skills/eclair-community-search/SKILL.md) | Use when a user wants to chercher sujets et messages selon les permissions on Éclair CMS 2.x; design a recherche de forum workflow with native extension compatibility, security and acceptance gates. |

## Applications métiers (8)

Réservations, abonnements, annuaires et outils métiers.

| Skill | Description (EN) |
|---|---|
| [`eclair-bookings`](../skills/eclair-bookings/SKILL.md) | Use when a user wants to gérer une ressource réservable sans doubles réservations on Éclair CMS 2.x; design a réservations métier workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-appointments-calendar`](../skills/eclair-appointments-calendar/SKILL.md) | Use when a user wants to prendre rendez-vous et intégrer calendriers externes on Éclair CMS 2.x; design a rendez-vous et calendrier workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-memberships`](../skills/eclair-memberships/SKILL.md) | Use when a user wants to gérer niveaux membres, échéances et droits d’accès on Éclair CMS 2.x; design a abonnements et adhésions workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-directory`](../skills/eclair-directory/SKILL.md) | Use when a user wants to créer fiches et filtres indexables on Éclair CMS 2.x; design a annuaire professionnel workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-events-ticketing`](../skills/eclair-events-ticketing/SKILL.md) | Use when a user wants to commercialiser places, billets et admissions on Éclair CMS 2.x; design a événements et billets workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-job-board`](../skills/eclair-job-board/SKILL.md) | Use when a user wants to publier annonces et candidatures respectueuses des données on Éclair CMS 2.x; design a offres d’emploi workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-real-estate`](../skills/eclair-real-estate/SKILL.md) | Use when a user wants to construire catalogue de biens avec recherche et contact on Éclair CMS 2.x; design a annonces immobilières workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-forms-crm`](../skills/eclair-forms-crm/SKILL.md) | Use when a user wants to collecter demandes et suivre leur traitement on Éclair CMS 2.x; design a formulaires et mini-crm workflow with native extension compatibility, security and acceptance gates. |

## Design et UX (7)

Thèmes, blocs, accessibilité et rapidité.

| Skill | Description (EN) |
|---|---|
| [`eclair-design`](../skills/eclair-design/SKILL.md) | Use when a user wants to créer des sites cohérents avec éclair design et le thème natif on Éclair CMS 2.x; design a direction artistique éclair workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-theme-builder`](../skills/eclair-theme-builder/SKILL.md) | Use when a user wants to produire un thème éclair v2 compatible avec mise à jour on Éclair CMS 2.x; design a création de thème workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-blocks-library`](../skills/eclair-blocks-library/SKILL.md) | Use when a user wants to composer des blocs de contenu et extensions éditables on Éclair CMS 2.x; design a bibliothèque de blocs workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-accessibility`](../skills/eclair-accessibility/SKILL.md) | Use when a user wants to auditer et corriger une interface éclair accessible on Éclair CMS 2.x; design a accessibilité wcag workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-design-system`](../skills/eclair-design-system/SKILL.md) | Use when a user wants to construire un langage visuel cohérent et maintenable on Éclair CMS 2.x; design a système de design workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-responsive-ux`](../skills/eclair-responsive-ux/SKILL.md) | Use when a user wants to optimiser navigation, formulaires et compositions mobiles on Éclair CMS 2.x; design a ux responsive workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-performance-ux`](../skills/eclair-performance-ux/SKILL.md) | Use when a user wants to mesurer et réduire poids et instabilité de pages on Éclair CMS 2.x; design a performance ux workflow with native extension compatibility, security and acceptance gates. |

## SEO, GEO et migration (5)

Indexabilité, données structurées et WordPress.

| Skill | Description (EN) |
|---|---|
| [`eclair-seo-audit`](../skills/eclair-seo-audit/SKILL.md) | Use when a user wants to vérifier indexabilité, canonical, robots, liens et performance on Éclair CMS 2.x; design a audit seo technique workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-geo-optimization`](../skills/eclair-geo-optimization/SKILL.md) | Use when a user wants to faciliter lisibilité des pages pour moteurs et assistants ia on Éclair CMS 2.x; design a geo et agents ia workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-wordpress-migration`](../skills/eclair-wordpress-migration/SKILL.md) | Use when a user wants to préserver les urls, contenus et trafic en migrant vers éclair 2 on Éclair CMS 2.x; design a migration wordpress workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-structured-data`](../skills/eclair-structured-data/SKILL.md) | Use when a user wants to ajouter ou vérifier schema.org cohérent avec le contenu on Éclair CMS 2.x; design a données structurées workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-multilingual-seo`](../skills/eclair-multilingual-seo/SKILL.md) | Use when a user wants to gérer plusieurs langues sans duplication ni mauvaises canonical on Éclair CMS 2.x; design a seo multilingue workflow with native extension compatibility, security and acceptance gates. |

## Intégrations et automatisations (6)

API, webhooks, emails, IA, suivi.

| Skill | Description (EN) |
|---|---|
| [`eclair-webhooks`](../skills/eclair-webhooks/SKILL.md) | Use when a user wants to relier applications externes par événements sûrs on Éclair CMS 2.x; design a webhooks entrants et sortants workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-email-automation`](../skills/eclair-email-automation/SKILL.md) | Use when a user wants to envoyer confirmations et relances fiables on Éclair CMS 2.x; design a emails transactionnels workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-api-integration`](../skills/eclair-api-integration/SKILL.md) | Use when a user wants to créer intégrations externes robustes et limitées on Éclair CMS 2.x; design a connecteurs api workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-crm-integration`](../skills/eclair-crm-integration/SKILL.md) | Use when a user wants to relier prospects/clients à un crm sans doublons on Éclair CMS 2.x; design a synchronisation crm workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-ai-workflows`](../skills/eclair-ai-workflows/SKILL.md) | Use when a user wants to automatiser aide éditoriale sans publication intempestive on Éclair CMS 2.x; design a workflows ia workflow with native extension compatibility, security and acceptance gates. |
| [`eclair-observability`](../skills/eclair-observability/SKILL.md) | Use when a user wants to surveiller santé, coûts et incidents des modules on Éclair CMS 2.x; design a observabilité et alertes workflow with native extension compatibility, security and acceptance gates. |

**Total : 57 skills.**
