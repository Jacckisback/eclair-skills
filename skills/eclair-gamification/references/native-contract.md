# Application du contrat natif au skill eclair-gamification

Ce skill utilise exclusivement ce que livre Éclair CMS 2.0.x : les fonctions du noyau, le contrat de thème et le contrat `eclair-extension/1`. Référence officielle : https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position de ce skill

Cette fonction demande des écritures de visiteurs, des comptes publics, des transactions ou des événements signés que `eclair-extension/1` ne fournit pas en 2.0. Livrer la conception, une maquette GET sûre et des tests bloquants ; ne jamais annoncer une mise en production.

## Garde-fou pratique

Sur un vrai checkout, relire `eclair/index.php`, exécuter `php tools/validate.php` sur tout paquet produit et `php tests/run.php`. Si la demande dépasse les fonctions natives, les routes GET publiques, les pages d'administration protégées, les blocs, les réglages et `Store`, produire une demande d'évolution distincte ; **ne jamais simuler sa disponibilité**.
