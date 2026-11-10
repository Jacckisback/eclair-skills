# Contrat de la famille Commerce Pro

Cible : **Éclair CMS 2.0.x**, extension **`eclair-extension/1`**, identifiants et version découverts avant toute modification.

**Capacités natives à privilégier :** fonctions déjà intégrées au noyau (voir `core-map.md`), thèmes dans `site/themes/`, extensions dans `site/extensions/`, données `Store` sous `$ctx['data']`, routes GET publiques et GET/POST d'administration protégées, tâches planifiées, migrations, validation `tools/validate.php`, suite PHP, mesures.

**Limitations de production :** Panier, commandes et paiements ont besoin de POST publics, d’un stockage transactionnel fiable, de webhooks authentifiés et d’idempotence; Éclair 2.0 officiel ne fournit pas tout cela. La PR #19 est encore un brouillon : ne jamais utiliser une route POST non fusionnée comme preuve de compatibilité.

**Politique agent :** utiliser d'abord le natif, générer le minimum de code, garder le noyau intact, refuser de présenter une maquette comme une fonctionnalité en service ; demander une évolution du noyau quand elle est nécessaire. Les changements à forte portée (paiement, contenu privé, e-mails, données personnelles ou de santé) exigent des tests réels et une validation humaine avant activation.

**Points de sécurité :** contrôler chaque objet et chaque écriture ; protéger formulaires, secrets, signatures et données personnelles ; vérifier erreurs et retour arrière ; ne garder en cache public que du HTML sans donnée d'utilisateur. Ne pas confondre `eclair-extension/1` et les API expérimentales antérieures.
