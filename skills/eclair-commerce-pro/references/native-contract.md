# Application du contrat natif au skill eclair-commerce-pro

Ce skill utilise exclusivement le contrat `eclair-extension/1` livré dans Éclair CMS 2.0.0 et non les API des anciens prototypes. Référence officielle : https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Garde-fou pratique

Sur un vrai checkout, relire `eclair/index.php`, exécuter `php tools/validate.php` sur tout paquet produit et `php tests/run.php`. Si le contrat demandé dépasse les routes GET publiques, les permissions admin, les champs/blocs et `Store`, produire une RFC distincte ; **ne jamais simuler sa disponibilité**.
