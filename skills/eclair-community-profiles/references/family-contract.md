# Contrat de la famille Forum et communauté

Cible : **Éclair CMS 2.0.x**, extension **`eclair-extension/1`**, identifiants et version découverts avant toute modification.

**Capacités natives à privilégier :** thèmes dans `site/themes/`, extensions dans `site/extensions/`, données `Store` sous `$ctx['data']`, routes GET publiques et GET/POST admin protégées, tâches optionnelles, migration du module, validation `tools/validate.php`, suite PHP, mesures.

**Limitations de production :** Les catégories et listes publiques peuvent être GET; publications, signalements, profils privés et modération exigent une identité et des routes d’écriture sûres, anti-spam et stockage adapté.

**Politique agent :** générer le minimum de code, garder le noyau intact, refuser de prétendre qu'un POC fournit une fonctionnalité transactionnelle; demander une PR/RFC noyau lorsque nécessaire. Les changements à haute portée (paiement, contenu privé, emails, données de santé, données clients) exigent tests réels et validation humaine avant activation.

**Points de sécurité :** contrôler chaque objet et chaque écriture; protéger les formulaires, secrets, signatures, données personnelles; vérifier les erreurs/rollback; conserver le HTML public cacheable seulement quand il ne contient aucune donnée utilisateur. Ne pas confondre `eclair-extension/1` et les APIs expérimentales antérieures.
