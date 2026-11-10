# Catalogue complet — Éclair Skills v2.2.0

Généré par `scripts/build_readmes.py` à partir de `catalog.json`. **200 Agent Skills = 200 guides pour agents, pas 200 extensions PHP.** Cible : Éclair CMS 2.0.x, contrat `eclair-extension/1`.

**Légende** — 🟣 **Intégré au noyau** : déjà présent dans Éclair 2.0 ; le skill le configure et le vérifie, sans extension. 🟢 **Natif v2** : réalisable aujourd’hui avec le contrat natif. 🔵 **Prototype lecture seule possible** : une version publique GET est faisable maintenant ; les écritures demandent plus. 🟠 **Conception · noyau requis** : conception et tests complets dès maintenant, la production exige des capacités pas encore présentes dans Éclair 2.0 (POST public, transactions, comptes membres…). 🟡 **Partiellement bloqué** : certaines parties dépendent d’une évolution du contrat du noyau.

## 🧱 Fondations (8)

Contrat natif v2, tests et sécurité.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-architecture`](../skills/eclair-architecture/SKILL.md) | Décider où placer une fonctionnalité (réglage, thème, extension ou RFC du noyau) sans toucher au cœur v2. | — | 🟢 Natif v2 |
| [`eclair-extension-builder`](../skills/eclair-extension-builder/SKILL.md) | Construire une extension v2 réellement installable : `extension.json`, `extension.php`, contrat `eclair-extension/1`. | — | 🟢 Natif v2 |
| [`eclair-storage`](../skills/eclair-storage/SKILL.md) | Choisir la bonne persistance, les migrations, sauvegardes et besoins SQL de chaque module. | — | 🟢 Natif v2 |
| [`eclair-auth-roles`](../skills/eclair-auth-roles/SKILL.md) | Distinguer les droits d’administration des membres, élèves, clients et modérateurs. | — | 🟢 Natif v2 |
| [`eclair-routing`](../skills/eclair-routing/SKILL.md) | Créer des routes publiques/admin en protégeant les URL existantes, les redirections et le SEO. | — | 🟢 Natif v2 |
| [`eclair-cache-contract`](../skills/eclair-cache-contract/SKILL.md) | Garder le cache rapide et sûr : invalidation, confidentialité et budgets de performance. | — | 🟢 Natif v2 |
| [`eclair-security-audit`](../skills/eclair-security-audit/SKILL.md) | Auditer une extension avant activation : chaîne d’approvisionnement, actions admin, données membres. | — | 🟢 Natif v2 |
| [`eclair-test-suite`](../skills/eclair-test-suite/SKILL.md) | Écrire les tests CI, de régression, sécurité et performance : une preuve avant publication. | — | 🟢 Natif v2 |

## 📝 Contenu et édition (14)

Articles, pages, catégories, menus, recherche, flux.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-blog-posts`](../skills/eclair-blog-posts/SKILL.md) | Publier et organiser des articles de blog avec l'éditeur de blocs natif. | Articles natifs de WordPress | 🟣 Intégré au noyau |
| [`eclair-static-pages`](../skills/eclair-static-pages/SKILL.md) | Créer les pages fixes du site (accueil, à propos, services, contact) et leur arborescence. | Pages natives de WordPress | 🟣 Intégré au noyau |
| [`eclair-categories`](../skills/eclair-categories/SKILL.md) | Structurer les contenus en catégories piliers utiles aux visiteurs et au SEO. | Catégories natives de WordPress | 🟣 Intégré au noyau |
| [`eclair-tags-taxonomies`](../skills/eclair-tags-taxonomies/SKILL.md) | Reprendre des étiquettes ou taxonomies personnalisées quand le noyau n'offre que des catégories. | Étiquettes et taxonomies personnalisées de WordPress | 🟡 Partiellement bloqué |
| [`eclair-custom-content-types`](../skills/eclair-custom-content-types/SKILL.md) | Modéliser des contenus métier (réalisations, biens, événements) sans type de contenu personnalisé dans le noyau. | Custom Post Types (CPT UI, ACF) | 🟡 Partiellement bloqué |
| [`eclair-custom-fields`](../skills/eclair-custom-fields/SKILL.md) | Ajouter des champs structurés à des blocs ou à des réglages d'extension. | Advanced Custom Fields, Meta Box | 🟢 Natif v2 |
| [`eclair-comments`](../skills/eclair-comments/SKILL.md) | Concevoir des commentaires d'articles avec modération et anti-spam. | Commentaires natifs, Akismet | 🟠 Conception · noyau requis |
| [`eclair-editorial-workflow`](../skills/eclair-editorial-workflow/SKILL.md) | Organiser brouillons, relecture et calendrier de publication d'une équipe. | Edit Flow, PublishPress, planification native | 🟣 Intégré au noyau |
| [`eclair-authors`](../skills/eclair-authors/SKILL.md) | Présenter les auteurs avec biographie et expertise vérifiables. | Profils d'auteur, boîtes auteur | 🟣 Intégré au noyau |
| [`eclair-navigation-menus`](../skills/eclair-navigation-menus/SKILL.md) | Construire des menus clairs pour l'en-tête et le pied de page. | Menus natifs de WordPress | 🟣 Intégré au noyau |
| [`eclair-site-search`](../skills/eclair-site-search/SKILL.md) | Offrir une recherche interne rapide sans base de données. | Recherche native, Relevanssi, SearchWP | 🟢 Natif v2 |
| [`eclair-rss-feeds`](../skills/eclair-rss-feeds/SKILL.md) | Vérifier et valoriser le flux RSS natif du site. | Flux natifs de WordPress | 🟣 Intégré au noyau |
| [`eclair-related-posts`](../skills/eclair-related-posts/SKILL.md) | Proposer des articles liés pertinents en fin de page. | YARPP, Jetpack Related Posts | 🟢 Natif v2 |
| [`eclair-table-of-contents`](../skills/eclair-table-of-contents/SKILL.md) | Ajouter un sommaire cliquable aux contenus longs. | Easy Table of Contents, LuckyWP | 🟢 Natif v2 |

## 🖼️ Médias (9)

Médiathèque, images, galeries, vidéo, audio, documents.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-media-library`](../skills/eclair-media-library/SKILL.md) | Organiser images et fichiers dans la médiathèque native. | Médiathèque de WordPress | 🟣 Intégré au noyau |
| [`eclair-image-optimization`](../skills/eclair-image-optimization/SKILL.md) | Tirer parti du WebP responsive et du chargement différé natifs. | Smush, ShortPixel, Imagify, EWWW | 🟣 Intégré au noyau |
| [`eclair-image-galleries`](../skills/eclair-image-galleries/SKILL.md) | Créer des galeries photo légères et accessibles. | Galerie native, NextGEN, Envira | 🟢 Natif v2 |
| [`eclair-video-embeds`](../skills/eclair-video-embeds/SKILL.md) | Intégrer des vidéos sans ralentir la page ni déposer de cookies. | Bloc vidéo et embeds de WordPress | 🟣 Intégré au noyau |
| [`eclair-audio-podcast`](../skills/eclair-audio-podcast/SKILL.md) | Publier des épisodes audio avec lecteur et flux de podcast. | PowerPress, Seriously Simple Podcasting | 🟢 Natif v2 |
| [`eclair-file-downloads`](../skills/eclair-file-downloads/SKILL.md) | Proposer des fichiers à télécharger (PDF, modèles, fiches). | Download Manager, Download Monitor | 🟢 Natif v2 |
| [`eclair-sliders-carousels`](../skills/eclair-sliders-carousels/SKILL.md) | Créer un diaporama sobre qui ne dégrade ni la vitesse ni l'accessibilité. | Slider Revolution, Smart Slider, MetaSlider | 🟢 Natif v2 |
| [`eclair-lightbox`](../skills/eclair-lightbox/SKILL.md) | Agrandir les images au clic avec une visionneuse légère. | Extensions de lightbox (FooBox, Simple Lightbox) | 🟢 Natif v2 |
| [`eclair-pdf-documents`](../skills/eclair-pdf-documents/SKILL.md) | Publier des PDF lisibles, accessibles et référencés. | PDF Embedder, visionneuses de documents | 🟢 Natif v2 |

## 🧩 Blocs et composants (14)

FAQ, onglets, tableaux, tarifs, sections, navigation.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-accordions-faq`](../skills/eclair-accordions-faq/SKILL.md) | Présenter questions et réponses avec le bloc FAQ natif. | Extensions d'accordéon et de FAQ | 🟣 Intégré au noyau |
| [`eclair-tabs`](../skills/eclair-tabs/SKILL.md) | Organiser un contenu en onglets accessibles. | Extensions d'onglets (Tabs, Kadence Blocks) | 🟢 Natif v2 |
| [`eclair-data-tables`](../skills/eclair-data-tables/SKILL.md) | Présenter des tableaux lisibles sur mobile. | TablePress, wpDataTables | 🟣 Intégré au noyau |
| [`eclair-pricing-tables`](../skills/eclair-pricing-tables/SKILL.md) | Présenter offres et tarifs de façon claire et honnête. | Extensions de tableaux de prix | 🟢 Natif v2 |
| [`eclair-timelines`](../skills/eclair-timelines/SKILL.md) | Raconter une histoire ou un processus en étapes datées. | Extensions de timeline | 🟢 Natif v2 |
| [`eclair-countdowns`](../skills/eclair-countdowns/SKILL.md) | Afficher un compte à rebours vers une date réelle. | Extensions de countdown | 🟢 Natif v2 |
| [`eclair-team-members`](../skills/eclair-team-members/SKILL.md) | Présenter l'équipe avec le bloc natif. | Extensions de présentation d'équipe | 🟣 Intégré au noyau |
| [`eclair-logo-walls`](../skills/eclair-logo-walls/SKILL.md) | Afficher des logos de clients ou partenaires autorisés. | Extensions de carrousel de logos | 🟢 Natif v2 |
| [`eclair-cta-sections`](../skills/eclair-cta-sections/SKILL.md) | Placer des appels à l'action clairs avec les blocs natifs. | Blocs bouton et bannières d'appel à l'action | 🟣 Intégré au noyau |
| [`eclair-hero-sections`](../skills/eclair-hero-sections/SKILL.md) | Composer une section d'ouverture forte avec le bloc natif. | Sections hero des constructeurs de pages | 🟣 Intégré au noyau |
| [`eclair-headers-footers`](../skills/eclair-headers-footers/SKILL.md) | Personnaliser en-tête et pied de page par un thème de site. | Constructeurs d'en-tête et de pied de page | 🟢 Natif v2 |
| [`eclair-breadcrumbs`](../skills/eclair-breadcrumbs/SKILL.md) | Vérifier le fil d'Ariane et son balisage natifs. | Fil d'Ariane de Yoast ou Breadcrumb NavXT | 🟣 Intégré au noyau |
| [`eclair-pagination`](../skills/eclair-pagination/SKILL.md) | Paginer les listes d'articles et de fiches proprement. | Pagination native, WP-PageNavi | 🟢 Natif v2 |
| [`eclair-dark-mode`](../skills/eclair-dark-mode/SKILL.md) | Proposer un mode sombre fidèle à la charte. | Extensions de dark mode | 🟢 Natif v2 |

## 🎨 Design et UX (7)

Thèmes, blocs, accessibilité, rapidité.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-design`](../skills/eclair-design/SKILL.md) | Direction artistique : créer des sites cohérents avec Éclair Design et le thème natif. | — | 🟢 Natif v2 |
| [`eclair-theme-builder`](../skills/eclair-theme-builder/SKILL.md) | Produire un thème Éclair v2 compatible avec les mises à jour. | — | 🟢 Natif v2 |
| [`eclair-blocks-library`](../skills/eclair-blocks-library/SKILL.md) | Composer des blocs de contenu et extensions éditables. | — | 🟢 Natif v2 |
| [`eclair-accessibility`](../skills/eclair-accessibility/SKILL.md) | Auditer et corriger une interface accessible (WCAG). | — | 🟢 Natif v2 |
| [`eclair-design-system`](../skills/eclair-design-system/SKILL.md) | Construire un langage visuel cohérent et maintenable (tokens, composants). | — | 🟢 Natif v2 |
| [`eclair-responsive-ux`](../skills/eclair-responsive-ux/SKILL.md) | Optimiser navigation, formulaires et mises en page mobiles. | — | 🟢 Natif v2 |
| [`eclair-performance-ux`](../skills/eclair-performance-ux/SKILL.md) | Mesurer et réduire le poids et l’instabilité des pages. | — | 🟢 Natif v2 |

## 🌍 Multilingue (6)

Langues, sélecteur, formats, adresses, traduction.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-multilingual-content`](../skills/eclair-multilingual-content/SKILL.md) | Publier un site en plusieurs langues avec des versions reliées. | WPML, Polylang, TranslatePress | 🟡 Partiellement bloqué |
| [`eclair-language-switcher`](../skills/eclair-language-switcher/SKILL.md) | Ajouter un sélecteur de langue clair et accessible. | Sélecteurs de langue de WPML ou Polylang | 🟢 Natif v2 |
| [`eclair-rtl-support`](../skills/eclair-rtl-support/SKILL.md) | Adapter le thème à l'arabe ou à l'hébreu. | Feuilles de style RTL des thèmes WordPress | 🟢 Natif v2 |
| [`eclair-locale-formats`](../skills/eclair-locale-formats/SKILL.md) | Afficher dates, nombres, prix et adresses au format de chaque pays. | Réglages régionaux de WordPress | 🟢 Natif v2 |
| [`eclair-translated-urls`](../skills/eclair-translated-urls/SKILL.md) | Traduire les adresses sans perdre le référencement. | Traduction des slugs (WPML, Polylang Pro) | 🟡 Partiellement bloqué |
| [`eclair-translation-workflow`](../skills/eclair-translation-workflow/SKILL.md) | Organiser traduction, relecture et mise à jour des versions. | Gestion de traduction (WPML, Weglot) | 🟢 Natif v2 |

## 📮 Formulaires (9)

Contact, devis, étapes, pièces jointes, sondages, calculs.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-contact-forms`](../skills/eclair-contact-forms/SKILL.md) | Mettre en place le formulaire de contact natif et sa boîte de réception. | Contact Form 7, WPForms | 🟣 Intégré au noyau |
| [`eclair-form-inbox`](../skills/eclair-form-inbox/SKILL.md) | Traiter les messages reçus sans en perdre. | Flamingo, entrées de formulaires | 🟣 Intégré au noyau |
| [`eclair-multi-step-forms`](../skills/eclair-multi-step-forms/SKILL.md) | Concevoir un formulaire long découpé en étapes. | Gravity Forms, Formidable Forms | 🟠 Conception · noyau requis |
| [`eclair-file-upload-forms`](../skills/eclair-file-upload-forms/SKILL.md) | Concevoir le dépôt de fichiers par les visiteurs en toute sécurité. | Champs de téléversement des extensions de formulaires | 🟠 Conception · noyau requis |
| [`eclair-payment-forms`](../skills/eclair-payment-forms/SKILL.md) | Encaisser un acompte, un don ou une prestation simple par lien de paiement. | WP Simple Pay, formulaires Stripe | 🔵 Prototype lecture seule possible |
| [`eclair-surveys-polls`](../skills/eclair-surveys-polls/SKILL.md) | Concevoir sondages et questionnaires de satisfaction. | WP Polls, Quiz and Survey Master | 🟠 Conception · noyau requis |
| [`eclair-quote-requests`](../skills/eclair-quote-requests/SKILL.md) | Recueillir des demandes de devis qualifiées. | Formulaires de devis, Request a Quote | 🔵 Prototype lecture seule possible |
| [`eclair-conditional-forms`](../skills/eclair-conditional-forms/SKILL.md) | Concevoir des formulaires dont les champs dépendent des réponses. | Logique conditionnelle de Gravity Forms ou WPForms | 🟠 Conception · noyau requis |
| [`eclair-calculators`](../skills/eclair-calculators/SKILL.md) | Proposer un simulateur de prix ou de mesure sans collecte de données. | Calculated Fields Form, Cost Calculator | 🟢 Natif v2 |

## 🔎 SEO, GEO et migration (11)

Indexabilité, données structurées, WordPress.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-seo-audit`](../skills/eclair-seo-audit/SKILL.md) | Vérifier indexabilité, canonical, robots, liens et performance. | — | 🟢 Natif v2 |
| [`eclair-geo-optimization`](../skills/eclair-geo-optimization/SKILL.md) | Rendre les pages lisibles par les moteurs et les assistants IA (GEO). | — | 🟢 Natif v2 |
| [`eclair-wordpress-migration`](../skills/eclair-wordpress-migration/SKILL.md) | Migrer depuis WordPress en préservant URL, contenus et trafic. | — | 🟢 Natif v2 |
| [`eclair-structured-data`](../skills/eclair-structured-data/SKILL.md) | Ajouter ou vérifier des données schema.org cohérentes avec le contenu. | — | 🟡 Partiellement bloqué |
| [`eclair-multilingual-seo`](../skills/eclair-multilingual-seo/SKILL.md) | Gérer plusieurs langues sans duplication ni mauvaises canonical (hreflang). | — | 🟢 Natif v2 |
| [`eclair-meta-tags`](../skills/eclair-meta-tags/SKILL.md) | Rédiger titres et descriptions avec l'analyse SEO native. | Yoast SEO, Rank Math, All in One SEO | 🟣 Intégré au noyau |
| [`eclair-xml-sitemaps`](../skills/eclair-xml-sitemaps/SKILL.md) | Vérifier le sitemap natif et le déclarer aux moteurs. | Sitemaps de Yoast, Google XML Sitemaps | 🟣 Intégré au noyau |
| [`eclair-redirects-manager`](../skills/eclair-redirects-manager/SKILL.md) | Gérer les redirections 301 avec le gestionnaire natif. | Redirection, Yoast Premium | 🟣 Intégré au noyau |
| [`eclair-local-seo`](../skills/eclair-local-seo/SKILL.md) | Rendre une entreprise locale visible avec les données natives. | Yoast Local SEO, Rank Math Local | 🟣 Intégré au noyau |
| [`eclair-social-previews`](../skills/eclair-social-previews/SKILL.md) | Soigner l'aperçu des pages partagées sur les réseaux et messageries. | Open Graph de Yoast, Social Warfare | 🟣 Intégré au noyau |
| [`eclair-internal-linking`](../skills/eclair-internal-linking/SKILL.md) | Relier les pages entre elles pour les visiteurs et les moteurs. | Link Whisper, Internal Link Juicer | 🟢 Natif v2 |

## 📣 Marketing et audience (12)

Newsletter, pages d’atterrissage, mesure, partage, publicité.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-newsletter-signup`](../skills/eclair-newsletter-signup/SKILL.md) | Recueillir des inscriptions à une newsletter dans les règles. | MailPoet, Mailchimp for WordPress | 🟡 Partiellement bloqué |
| [`eclair-email-campaigns`](../skills/eclair-email-campaigns/SKILL.md) | Concevoir l'envoi de campagnes e-mail depuis les contenus du site. | MailPoet, Newsletter, FluentCRM | 🟠 Conception · noyau requis |
| [`eclair-popups-optins`](../skills/eclair-popups-optins/SKILL.md) | Afficher un encart d'incitation discret et respectueux. | Popup Maker, OptinMonster | 🟢 Natif v2 |
| [`eclair-landing-pages`](../skills/eclair-landing-pages/SKILL.md) | Composer une page d'atterrissage ciblée avec les blocs natifs. | Elementor, SeedProd, Leadpages | 🟣 Intégré au noyau |
| [`eclair-ab-testing`](../skills/eclair-ab-testing/SKILL.md) | Concevoir des tests A/B compatibles avec un site servi en cache. | Nelio A/B Testing, Google Optimize (arrêté) | 🟠 Conception · noyau requis |
| [`eclair-privacy-analytics`](../skills/eclair-privacy-analytics/SKILL.md) | Mesurer l'audience sans cookies ni profilage. | Matomo, Plausible, Koko Analytics | 🟡 Partiellement bloqué |
| [`eclair-social-sharing`](../skills/eclair-social-sharing/SKILL.md) | Ajouter des liens de partage sans script tiers. | AddToAny, Social Warfare | 🟢 Natif v2 |
| [`eclair-social-feeds`](../skills/eclair-social-feeds/SKILL.md) | Afficher ses dernières publications sociales sans alourdir le site. | Smash Balloon, flux Instagram | 🟡 Partiellement bloqué |
| [`eclair-testimonials`](../skills/eclair-testimonials/SKILL.md) | Présenter des témoignages authentiques de clients. | Strong Testimonials, extensions d'avis | 🟢 Natif v2 |
| [`eclair-affiliate-links`](../skills/eclair-affiliate-links/SKILL.md) | Gérer des liens affiliés avec les mentions légales natives. | ThirstyAffiliates, Pretty Links, AAWP | 🟣 Intégré au noyau |
| [`eclair-ads-adsense`](../skills/eclair-ads-adsense/SKILL.md) | Afficher de la publicité en règle sur les articles. | Ad Inserter, Site Kit, Advanced Ads | 🟣 Intégré au noyau |
| [`eclair-announcement-bars`](../skills/eclair-announcement-bars/SKILL.md) | Afficher un bandeau d'information temporaire. | Hello Bar, bandeaux de notification | 🟢 Natif v2 |

## 🛒 Commerce Pro (22)

Boutique transactionnelle et paiement, conçus avant déploiement.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-commerce-pro`](../skills/eclair-commerce-pro/SKILL.md) | Concevoir une boutique complète, du catalogue à la commande livrée (point d’entrée de la famille). | — | 🟠 Conception · noyau requis |
| [`eclair-product-catalog`](../skills/eclair-product-catalog/SKILL.md) | Construire un catalogue produits public rapide et indexable. | — | 🟣 Intégré au noyau |
| [`eclair-product-variants`](../skills/eclair-product-variants/SKILL.md) | Modéliser tailles, couleurs et configurations sans erreur de prix. | — | 🟣 Intégré au noyau |
| [`eclair-cart-checkout`](../skills/eclair-cart-checkout/SKILL.md) | Concevoir panier et tunnel de commande multi-lignes, avec prix et stock cohérents. | — | 🟠 Conception · noyau requis |
| [`eclair-orders-payments`](../skills/eclair-orders-payments/SKILL.md) | Implémenter les états de commande et les prestataires de paiement (PSP) avec webhooks signés. | — | 🟠 Conception · noyau requis |
| [`eclair-tax-invoicing`](../skills/eclair-tax-invoicing/SKILL.md) | Préparer les points de branchement TVA et facturation adaptés à chaque juridiction (pas de taux universel). | — | 🟠 Conception · noyau requis |
| [`eclair-inventory`](../skills/eclair-inventory/SKILL.md) | Synchroniser le stock réel entre produits, variantes et commandes. | — | 🟠 Conception · noyau requis |
| [`eclair-shipping`](../skills/eclair-shipping/SKILL.md) | Gérer zones, tarifs, suivi et états de livraison. | — | 🟠 Conception · noyau requis |
| [`eclair-discounts`](../skills/eclair-discounts/SKILL.md) | Créer remises et coupons cohérents, jamais cumulés par erreur. | — | 🟠 Conception · noyau requis |
| [`eclair-commerce-analytics`](../skills/eclair-commerce-analytics/SKILL.md) | Suivre ventes et conversions sans exposer les données clients. | — | 🟠 Conception · noyau requis |
| [`eclair-shop-setup`](../skills/eclair-shop-setup/SKILL.md) | Ouvrir la boutique légère native avec ses pages légales. | WooCommerce (installation et réglages) | 🟣 Intégré au noyau |
| [`eclair-payment-links`](../skills/eclair-payment-links/SKILL.md) | Relier chaque produit à un lien de paiement du prestataire. | Passerelles Stripe et PayPal pour WooCommerce | 🟣 Intégré au noyau |
| [`eclair-merchant-feed`](../skills/eclair-merchant-feed/SKILL.md) | Diffuser les produits dans les comparateurs grâce au flux natif. | Product Feed PRO, Google Listings and Ads | 🟣 Intégré au noyau |
| [`eclair-subscriptions-billing`](../skills/eclair-subscriptions-billing/SKILL.md) | Concevoir des abonnements récurrents gérés par le prestataire de paiement. | WooCommerce Subscriptions | 🟠 Conception · noyau requis |
| [`eclair-digital-downloads`](../skills/eclair-digital-downloads/SKILL.md) | Concevoir la vente de fichiers avec livraison sécurisée. | Easy Digital Downloads | 🟠 Conception · noyau requis |
| [`eclair-wishlists`](../skills/eclair-wishlists/SKILL.md) | Concevoir des listes de favoris pour les visiteurs. | YITH WooCommerce Wishlist | 🟠 Conception · noyau requis |
| [`eclair-product-reviews`](../skills/eclair-product-reviews/SKILL.md) | Concevoir des avis clients vérifiés et modérés. | Avis natifs de WooCommerce, Judge.me | 🟠 Conception · noyau requis |
| [`eclair-product-filters`](../skills/eclair-product-filters/SKILL.md) | Aider à trouver un produit par filtres et tri. | Filtres de produits WooCommerce, FacetWP | 🔵 Prototype lecture seule possible |
| [`eclair-abandoned-cart`](../skills/eclair-abandoned-cart/SKILL.md) | Concevoir la relance des achats non terminés. | Extensions de panier abandonné | 🟠 Conception · noyau requis |
| [`eclair-gift-cards`](../skills/eclair-gift-cards/SKILL.md) | Concevoir la vente et l'utilisation de cartes cadeaux. | Extensions de cartes cadeaux | 🟠 Conception · noyau requis |
| [`eclair-customer-accounts`](../skills/eclair-customer-accounts/SKILL.md) | Concevoir l'espace client : commandes, adresses, factures. | Mon compte de WooCommerce | 🟠 Conception · noyau requis |
| [`eclair-returns-refunds`](../skills/eclair-returns-refunds/SKILL.md) | Organiser retours et remboursements de façon claire. | Extensions de gestion des retours | 🟠 Conception · noyau requis |

## 🎓 LMS (10)

Cours, inscriptions, progression, certifications.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-lms`](../skills/eclair-lms/SKILL.md) | Structurer une école en ligne modulaire (point d’entrée de la famille). | — | 🟠 Conception · noyau requis |
| [`eclair-course-builder`](../skills/eclair-course-builder/SKILL.md) | Composer cours, sections et leçons versionnés. | — | 🟠 Conception · noyau requis |
| [`eclair-lessons-media`](../skills/eclair-lessons-media/SKILL.md) | Fournir vidéos et documents protégés pour les cours. | — | 🟠 Conception · noyau requis |
| [`eclair-enrollment-access`](../skills/eclair-enrollment-access/SKILL.md) | Lier un achat ou une validation à une inscription et à ses autorisations. | — | 🟠 Conception · noyau requis |
| [`eclair-progress`](../skills/eclair-progress/SKILL.md) | Suivre la progression sans perte ni mise à jour incohérente. | — | 🟠 Conception · noyau requis |
| [`eclair-quizzes-certificates`](../skills/eclair-quizzes-certificates/SKILL.md) | Créer évaluations, seuils de réussite et attestations contrôlées. | — | 🟠 Conception · noyau requis |
| [`eclair-lms-analytics`](../skills/eclair-lms-analytics/SKILL.md) | Analyser complétion et engagement sans surveillance abusive. | — | 🟠 Conception · noyau requis |
| [`eclair-assignments`](../skills/eclair-assignments/SKILL.md) | Concevoir le dépôt de devoirs et leur correction. | Devoirs de LearnDash ou Tutor LMS | 🟠 Conception · noyau requis |
| [`eclair-live-classes`](../skills/eclair-live-classes/SKILL.md) | Annoncer et organiser des classes en visioconférence. | Intégrations Zoom des LMS | 🔵 Prototype lecture seule possible |
| [`eclair-drip-content`](../skills/eclair-drip-content/SKILL.md) | Concevoir l'ouverture progressive des leçons. | Drip content de LearnDash ou MemberPress | 🟠 Conception · noyau requis |

## 💬 Forum et communauté (10)

Discussions, modération, profils, notifications.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-forum`](../skills/eclair-forum/SKILL.md) | Concevoir des discussions publiques et privées avec modération (point d’entrée de la famille). | — | 🟠 Conception · noyau requis |
| [`eclair-discussions-topics`](../skills/eclair-discussions-topics/SKILL.md) | Gérer création, édition et état des sujets et réponses. | — | 🟠 Conception · noyau requis |
| [`eclair-community-profiles`](../skills/eclair-community-profiles/SKILL.md) | Proposer des profils publics choisis, séparés des données privées. | — | 🟠 Conception · noyau requis |
| [`eclair-moderation`](../skills/eclair-moderation/SKILL.md) | Construire les outils de retrait, signalement et appel. | — | 🟠 Conception · noyau requis |
| [`eclair-notifications`](../skills/eclair-notifications/SKILL.md) | Informer les membres sans spam ni fuite de données. | — | 🟠 Conception · noyau requis |
| [`eclair-community-search`](../skills/eclair-community-search/SKILL.md) | Chercher sujets et messages selon les permissions. | — | 🟠 Conception · noyau requis |
| [`eclair-private-messaging`](../skills/eclair-private-messaging/SKILL.md) | Concevoir des messages privés entre membres. | Messages privés de BuddyPress | 🟠 Conception · noyau requis |
| [`eclair-groups`](../skills/eclair-groups/SKILL.md) | Concevoir des groupes publics ou privés de membres. | Groupes de BuddyPress, BuddyBoss | 🟠 Conception · noyau requis |
| [`eclair-activity-feed`](../skills/eclair-activity-feed/SKILL.md) | Concevoir un fil d'activité de la communauté. | Flux d'activité de BuddyPress | 🟠 Conception · noyau requis |
| [`eclair-gamification`](../skills/eclair-gamification/SKILL.md) | Concevoir points, badges et classements motivants. | GamiPress, myCred | 🟠 Conception · noyau requis |

## 🗂️ Applications métiers (20)

Réservations, abonnements, annuaires, outils métiers.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-bookings`](../skills/eclair-bookings/SKILL.md) | Gérer une ressource réservable sans double réservation. | — | 🟠 Conception · noyau requis |
| [`eclair-appointments-calendar`](../skills/eclair-appointments-calendar/SKILL.md) | Prendre rendez-vous et intégrer des calendriers externes. | — | 🟠 Conception · noyau requis |
| [`eclair-memberships`](../skills/eclair-memberships/SKILL.md) | Gérer niveaux d’adhésion, échéances et droits d’accès. | — | 🟠 Conception · noyau requis |
| [`eclair-directory`](../skills/eclair-directory/SKILL.md) | Créer les fiches et filtres indexables d’un annuaire professionnel. | — | 🔵 Prototype lecture seule possible |
| [`eclair-events-ticketing`](../skills/eclair-events-ticketing/SKILL.md) | Commercialiser places, billets et admissions pour des événements. | — | 🟠 Conception · noyau requis |
| [`eclair-job-board`](../skills/eclair-job-board/SKILL.md) | Publier offres d’emploi et candidatures respectueuses des données. | — | 🟠 Conception · noyau requis |
| [`eclair-real-estate`](../skills/eclair-real-estate/SKILL.md) | Construire un catalogue de biens immobiliers avec recherche et contact. | — | 🟠 Conception · noyau requis |
| [`eclair-forms-crm`](../skills/eclair-forms-crm/SKILL.md) | Collecter des demandes par formulaire et suivre leur traitement (mini-CRM). | — | 🟠 Conception · noyau requis |
| [`eclair-restaurant-menu`](../skills/eclair-restaurant-menu/SKILL.md) | Publier la carte et les menus d'un restaurant. | Extensions de menu de restaurant | 🟢 Natif v2 |
| [`eclair-recipes`](../skills/eclair-recipes/SKILL.md) | Publier des recettes claires et bien structurées. | WP Recipe Maker, Tasty Recipes | 🟢 Natif v2 |
| [`eclair-hotel-rooms`](../skills/eclair-hotel-rooms/SKILL.md) | Présenter chambres ou locations et diriger vers la réservation. | Extensions de réservation hôtelière | 🔵 Prototype lecture seule possible |
| [`eclair-professional-services`](../skills/eclair-professional-services/SKILL.md) | Construire le site d'un cabinet ou d'un indépendant réglementé. | Thèmes pour avocats, médecins, consultants | 🟢 Natif v2 |
| [`eclair-nonprofit-donations`](../skills/eclair-nonprofit-donations/SKILL.md) | Présenter une association et recevoir des dons par lien de paiement. | GiveWP, Charitable | 🔵 Prototype lecture seule possible |
| [`eclair-classifieds`](../skills/eclair-classifieds/SKILL.md) | Concevoir un site de petites annonces déposées par les visiteurs. | Extensions de petites annonces | 🟠 Conception · noyau requis |
| [`eclair-knowledge-base`](../skills/eclair-knowledge-base/SKILL.md) | Créer une documentation ou un centre d'aide. | BetterDocs, Echo Knowledge Base | 🟢 Natif v2 |
| [`eclair-helpdesk-tickets`](../skills/eclair-helpdesk-tickets/SKILL.md) | Concevoir un suivi des demandes d'assistance. | Awesome Support, SupportCandy | 🟠 Conception · noyau requis |
| [`eclair-magazine-news`](../skills/eclair-magazine-news/SKILL.md) | Monter un site d'actualités ou un magazine en ligne. | Thèmes magazine (Newspaper, GeneratePress) | 🟢 Natif v2 |
| [`eclair-portfolio`](../skills/eclair-portfolio/SKILL.md) | Présenter des réalisations avec études de cas. | Extensions de portfolio | 🟢 Natif v2 |
| [`eclair-coupons-deals`](../skills/eclair-coupons-deals/SKILL.md) | Publier des offres et codes promotionnels à jour. | Extensions de sites de coupons | 🟢 Natif v2 |
| [`eclair-glossary`](../skills/eclair-glossary/SKILL.md) | Créer un glossaire de termes du métier. | Extensions de glossaire | 🟢 Natif v2 |

## 🔌 Intégrations et automatisations (15)

API, webhooks, emails, IA, supervision.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-webhooks`](../skills/eclair-webhooks/SKILL.md) | Relier des applications externes par des événements sûrs, signés et idempotents. | — | 🟠 Conception · noyau requis |
| [`eclair-email-automation`](../skills/eclair-email-automation/SKILL.md) | Envoyer des confirmations et relances fiables (emails transactionnels). | — | 🟠 Conception · noyau requis |
| [`eclair-api-integration`](../skills/eclair-api-integration/SKILL.md) | Créer des connecteurs API externes robustes et limités. | — | 🟠 Conception · noyau requis |
| [`eclair-crm-integration`](../skills/eclair-crm-integration/SKILL.md) | Synchroniser prospects et clients avec un CRM, sans doublons. | — | 🟠 Conception · noyau requis |
| [`eclair-ai-workflows`](../skills/eclair-ai-workflows/SKILL.md) | Automatiser l’aide éditoriale par IA, sans publication sans humain. | — | 🟠 Conception · noyau requis |
| [`eclair-observability`](../skills/eclair-observability/SKILL.md) | Surveiller santé, coûts et incidents des modules, avec alertes. | — | 🟠 Conception · noyau requis |
| [`eclair-google-analytics`](../skills/eclair-google-analytics/SKILL.md) | Relier Google Analytics en respectant consentement et politique de sécurité. | Site Kit, MonsterInsights | 🟡 Partiellement bloqué |
| [`eclair-search-console`](../skills/eclair-search-console/SKILL.md) | Vérifier le site dans les outils des moteurs et suivre son indexation. | Site Kit, vérification par Yoast | 🟢 Natif v2 |
| [`eclair-tag-manager`](../skills/eclair-tag-manager/SKILL.md) | Évaluer l'usage d'un gestionnaire de balises sur un site strict. | Google Tag Manager, GTM4WP | 🟡 Partiellement bloqué |
| [`eclair-email-marketing-providers`](../skills/eclair-email-marketing-providers/SKILL.md) | Relier le site à un service d'e-mailing (Brevo, Mailchimp ou autre). | Extensions officielles Brevo ou Mailchimp | 🟡 Partiellement bloqué |
| [`eclair-automation-platforms`](../skills/eclair-automation-platforms/SKILL.md) | Relier le site à Make, Zapier ou n8n. | Zapier for WordPress, Uncanny Automator | 🔵 Prototype lecture seule possible |
| [`eclair-maps-embeds`](../skills/eclair-maps-embeds/SKILL.md) | Afficher un plan d'accès sans pister les visiteurs. | Extensions Google Maps, Leaflet Map | 🟡 Partiellement bloqué |
| [`eclair-social-login`](../skills/eclair-social-login/SKILL.md) | Concevoir la connexion des membres avec Google, Apple ou autre. | Nextend Social Login | 🟠 Conception · noyau requis |
| [`eclair-live-chat`](../skills/eclair-live-chat/SKILL.md) | Proposer un contact immédiat sans widget lourd. | Tidio, Crisp, tawk.to | 🟡 Partiellement bloqué |
| [`eclair-calendar-feeds`](../skills/eclair-calendar-feeds/SKILL.md) | Publier un calendrier auquel on peut s'abonner. | The Events Calendar (export iCal) | 🟢 Natif v2 |

## ⚡ Performance (7)

Cache, CDN, images, poids, signaux web essentiels.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-page-cache`](../skills/eclair-page-cache/SKILL.md) | Vérifier que le cache statique natif sert bien chaque page publique. | WP Rocket, W3 Total Cache, LiteSpeed Cache | 🟣 Intégré au noyau |
| [`eclair-cdn`](../skills/eclair-cdn/SKILL.md) | Placer le site derrière un CDN sans casser cache ni sécurité. | Cloudflare, extensions CDN | 🟢 Natif v2 |
| [`eclair-lazy-loading`](../skills/eclair-lazy-loading/SKILL.md) | Contrôler le chargement différé natif des images et vidéos. | Lazy Load, a3 Lazy Load | 🟣 Intégré au noyau |
| [`eclair-asset-budget`](../skills/eclair-asset-budget/SKILL.md) | Tenir un budget de poids pour CSS, JavaScript et images. | Autoptimize, Asset CleanUp | 🟢 Natif v2 |
| [`eclair-core-web-vitals`](../skills/eclair-core-web-vitals/SKILL.md) | Mesurer et améliorer les signaux web essentiels sur de vraies pages. | Extensions d'optimisation des Core Web Vitals | 🟢 Natif v2 |
| [`eclair-fonts-loading`](../skills/eclair-fonts-loading/SKILL.md) | Choisir et charger les polices sans ralentir ni dépendre d'un tiers. | OMGF, polices locales | 🟣 Intégré au noyau |
| [`eclair-third-party-scripts`](../skills/eclair-third-party-scripts/SKILL.md) | Décider quels scripts tiers ajouter et à quel coût. | Insert Headers and Footers, WPCode | 🟡 Partiellement bloqué |

## 🛡️ Sécurité et confidentialité (9)

Connexion, 2FA, spam, en-têtes, intégrité, données personnelles.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-login-protection`](../skills/eclair-login-protection/SKILL.md) | Vérifier les protections natives de la page de connexion. | Limit Login Attempts, Wordfence Login Security | 🟣 Intégré au noyau |
| [`eclair-two-factor-auth`](../skills/eclair-two-factor-auth/SKILL.md) | Activer la double authentification native pour toute l'équipe. | Two Factor, WP 2FA | 🟣 Intégré au noyau |
| [`eclair-anti-spam`](../skills/eclair-anti-spam/SKILL.md) | Limiter le spam des formulaires sans pister les visiteurs. | Akismet, Antispam Bee | 🟣 Intégré au noyau |
| [`eclair-captcha`](../skills/eclair-captcha/SKILL.md) | Choisir une protection anti-robots compatible avec la politique de sécurité. | reCAPTCHA, hCaptcha, Turnstile | 🟡 Partiellement bloqué |
| [`eclair-security-headers`](../skills/eclair-security-headers/SKILL.md) | Contrôler les en-têtes de sécurité et la politique de contenu natifs. | HTTP Headers, Really Simple SSL | 🟣 Intégré au noyau |
| [`eclair-file-integrity`](../skills/eclair-file-integrity/SKILL.md) | Détecter toute modification du code avec le contrôle d'intégrité natif. | Wordfence Scan, Sucuri Security | 🟣 Intégré au noyau |
| [`eclair-cookie-consent`](../skills/eclair-cookie-consent/SKILL.md) | Rester sans bandeau quand c'est possible, et conforme quand un traceur est ajouté. | CookieYes, Complianz, Cookie Notice | 🟢 Natif v2 |
| [`eclair-privacy-requests`](../skills/eclair-privacy-requests/SKILL.md) | Traiter les demandes d'accès et d'effacement des données personnelles. | Outils de confidentialité de WordPress | 🟢 Natif v2 |
| [`eclair-incident-recovery`](../skills/eclair-incident-recovery/SKILL.md) | Réagir à un piratage ou à une fuite avec méthode. | Nettoyage de site piraté (Wordfence, Sucuri) | 🟢 Natif v2 |

## 🛠️ Administration et maintenance (10)

Comptes, sauvegardes, mises à jour, déménagement, journal.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-team-accounts`](../skills/eclair-team-accounts/SKILL.md) | Créer les comptes de l'équipe avec les droits strictement nécessaires. | Utilisateurs et rôles de WordPress, User Role Editor | 🟣 Intégré au noyau |
| [`eclair-backups-restore`](../skills/eclair-backups-restore/SKILL.md) | Planifier les sauvegardes natives et prouver qu'on sait restaurer. | UpdraftPlus, BackWPup, Duplicator | 🟣 Intégré au noyau |
| [`eclair-updates-rollback`](../skills/eclair-updates-rollback/SKILL.md) | Appliquer les mises à jour signées du noyau en sécurité. | Mises à jour de WordPress, Easy Updates Manager | 🟣 Intégré au noyau |
| [`eclair-maintenance-mode`](../skills/eclair-maintenance-mode/SKILL.md) | Afficher une page de maintenance propre pendant des travaux. | WP Maintenance Mode, SeedProd | 🟢 Natif v2 |
| [`eclair-staging-deploy`](../skills/eclair-staging-deploy/SKILL.md) | Tester les changements sur une copie avant la mise en ligne. | WP Staging, environnements de préproduction | 🟢 Natif v2 |
| [`eclair-site-migration`](../skills/eclair-site-migration/SKILL.md) | Déménager un site Éclair sans perte de contenus ni de référencement. | Duplicator, All-in-One WP Migration | 🟣 Intégré au noyau |
| [`eclair-error-pages`](../skills/eclair-error-pages/SKILL.md) | Soigner les pages 404 et d'erreur pour garder les visiteurs. | Gabarit 404 des thèmes, extensions 404 | 🟢 Natif v2 |
| [`eclair-site-settings`](../skills/eclair-site-settings/SKILL.md) | Régler identité, coordonnées, langue et apparence du site. | Réglages généraux et personnalisateur de WordPress | 🟣 Intégré au noyau |
| [`eclair-activity-log`](../skills/eclair-activity-log/SKILL.md) | Suivre qui a fait quoi grâce au journal natif. | WP Activity Log, Simple History | 🟣 Intégré au noyau |
| [`eclair-scheduled-tasks`](../skills/eclair-scheduled-tasks/SKILL.md) | Automatiser des traitements périodiques par les tâches d'extension. | WP-Cron, WP Crontrol | 🟢 Natif v2 |

## 💻 Développement et outils (7)

API en lecture, Markdown, MCP, ligne de commande, portage.

| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |
|---|---|---|---|
| [`eclair-public-api`](../skills/eclair-public-api/SKILL.md) | Exposer des données publiques du site en JSON. | API REST de WordPress | 🔵 Prototype lecture seule possible |
| [`eclair-headless-content`](../skills/eclair-headless-content/SKILL.md) | Réutiliser les contenus hors du site grâce aux versions Markdown et aux flux natifs. | WordPress headless, WPGraphQL | 🟢 Natif v2 |
| [`eclair-mcp-connector`](../skills/eclair-mcp-connector/SKILL.md) | Relier un assistant IA au site par le connecteur MCP natif. | Extensions d'assistant IA pour WordPress | 🟣 Intégré au noyau |
| [`eclair-cli-tools`](../skills/eclair-cli-tools/SKILL.md) | Utiliser les outils du dépôt pour valider, tester et mesurer. | WP-CLI | 🟢 Natif v2 |
| [`eclair-debugging-logs`](../skills/eclair-debugging-logs/SKILL.md) | Diagnostiquer une panne sans exposer d'informations sensibles. | WP_DEBUG, Query Monitor | 🟢 Natif v2 |
| [`eclair-local-development`](../skills/eclair-local-development/SKILL.md) | Monter un environnement local identique à la production. | Local, DevKinsta, environnements Docker | 🟢 Natif v2 |
| [`eclair-wp-plugin-porting`](../skills/eclair-wp-plugin-porting/SKILL.md) | Remplacer une extension WordPress par son équivalent Éclair. | Toute extension WordPress à remplacer | 🟢 Natif v2 |

**Total : 200 skills.**
