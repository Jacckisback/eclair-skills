# Application du contrat natif au skill eclair-translated-urls

Ce skill utilise exclusivement ce que livre Éclair CMS 2.0.x : les fonctions du noyau, le contrat de thème et le contrat `eclair-extension/1`. Référence officielle : https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position de ce skill

Une partie dépend d'un point d'accroche absent du contrat 2.0 (types de contenu, contribution SEO ou JSON-LD, politique de contenu par fonction, filtre de rendu). Livrer la partie native et documenter précisément l'écart, sans contournement.

## Garde-fou pratique

Sur un vrai checkout, relire `eclair/index.php`, exécuter `php tools/validate.php` sur tout paquet produit et `php tests/run.php`. Si la demande dépasse les fonctions natives, les routes GET publiques, les pages d'administration protégées, les blocs, les réglages et `Store`, produire une demande d'évolution distincte ; **ne jamais simuler sa disponibilité**.
