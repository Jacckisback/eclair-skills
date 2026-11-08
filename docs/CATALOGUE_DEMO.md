# Catalogue Demo — exemple natif sûr

Ce module fournit uniquement une route publique GET `/catalogue-demo` en lecture seule et démonstrative. Il **ne vend rien**. Pour être compatible avec le manifeste natif, les empreintes sont enregistrées dans `extension.json`, et le module n'exécute aucune opération à l'import.

Le fichier README n'est **pas inclus** dans l'archive installable de l'extension, puisque le manifeste `files` ne référence que `extension.php`.

Validation sur un checkout du CMS : `php tools/validate.php /chemin/catalogue-demo --json`. Le dossier doit alors contenir **seulement** `extension.json` et `extension.php` (ou bien ajouter toute ressource auxiliaire à `files`).

Usage : exemple de la famille Commerce Pro, sans transaction, sans création de compte ni module de paiement.
