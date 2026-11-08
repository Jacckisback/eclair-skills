# Release — Éclair Skills Foundations v1.1.0

**État : development-only, experimental.** Cible : Éclair CMS **2.0.0** (commit lu: `0beb440655090fbd9c3b58e8c56dca7ddbb2106e`).

Livraison : 8 skills Agent Skills actualisés, extension `member-directory` v0.2, RFC de routes publiques POST, script de patch sûr (branche Git de développement), scénarios PHP isolés et tests Python.

Le parcours actuellement démontré : GET formulaire connexion, POST connexion CSRF + TLS + limitation de tentatives, GET espace membre privé noindex/no-store, POST déconnexion avec CSRF formulaire ET session. Comptes admin/éditeur indépendants. **Aucune inscription publique, aucun email envoyé, aucune récupération de compte**.

Ce script de patch n’a PAS été appliqué à un checkout officiel complet ni soumis à GitHub. Les tests synthétiques démontrent l'applicabilité des ancres, pas la compatibilité réelle du CMS.

Contrôles : tests PHP du module et des comptes, validateur d'archive autonome, tests de patch Git (main, version incorrecte, dépôt sale, source inattendue, dry-run et branche expérimentale).

**Bloquants** : validateur natif officiel, tests HTTP/TLS sur pile réelle, test de compilation et non-régression du noyau, budgets, revue de sécurité indépendante, email/invitation, base transactionnelle avant production.
