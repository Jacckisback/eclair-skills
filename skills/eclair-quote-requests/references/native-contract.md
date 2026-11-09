# Application du contrat natif au skill eclair-quote-requests

Ce skill utilise exclusivement ce que livre Éclair CMS 2.0.x : les fonctions du noyau, le contrat de thème et le contrat `eclair-extension/1`. Référence officielle : https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position de ce skill

La lecture publique (GET, cacheable) est réalisable aujourd'hui. Toute écriture par un visiteur exige une route POST publique que le noyau 2.0 n'ouvre pas aux extensions (PR #19 en brouillon, non fusionnée) : ne pas la simuler.

## Garde-fou pratique

Sur un vrai checkout, relire `eclair/index.php`, exécuter `php tools/validate.php` sur tout paquet produit et `php tests/run.php`. Si la demande dépasse les fonctions natives, les routes GET publiques, les pages d'administration protégées, les blocs, les réglages et `Store`, produire une demande d'évolution distincte ; **ne jamais simuler sa disponibilité**.
