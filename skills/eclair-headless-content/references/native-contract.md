# Application du contrat natif au skill eclair-headless-content

Ce skill utilise exclusivement ce que livre Éclair CMS 2.0.x : les fonctions du noyau, le contrat de thème et le contrat `eclair-extension/1`. Référence officielle : https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position de ce skill

Réalisable avec `eclair-extension/1` et le contrat de thème : routes GET publiques cacheables, pages d'administration protégées, blocs et réglages déclaratifs, tâches planifiées, actifs. Vérifier d'abord qu'un bloc ou un réglage natif ne suffit pas.

## Garde-fou pratique

Sur un vrai checkout, relire `eclair/index.php`, exécuter `php tools/validate.php` sur tout paquet produit et `php tests/run.php`. Si la demande dépasse les fonctions natives, les routes GET publiques, les pages d'administration protégées, les blocs, les réglages et `Store`, produire une demande d'évolution distincte ; **ne jamais simuler sa disponibilité**.
