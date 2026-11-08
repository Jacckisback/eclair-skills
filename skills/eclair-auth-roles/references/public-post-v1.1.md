# Public member HTTP routes — Éclair 2.0.0 experimental

Le prototype v1.1 possède des handlers publics GET formulaire + POST connexion/déconnexion + GET espace privé. Ils ne sont valides qu’après l’ajout approuvé du contrat POST. Sessions membres distinctes des admins, jeton opaque, CSRF double-submit et CSRF de session à la déconnexion; aucun rôle admin/editor accordé.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
