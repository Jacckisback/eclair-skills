# Éclair Skills v1.3 — intégration native (8 novembre 2026)

## Livraison GitHub

- Dépôt : https://github.com/Jacckisback/eclair-cms
- Base : Éclair 2.0.0, commit `0beb440655090fbd9c3b58e8c56dca7ddbb2106e`
- Branche : `codex/eclair-skills-v1-3-public-member-post`
- PR en **brouillon**, non fusionnée : https://github.com/Jacckisback/eclair-cms/pull/19
- Commit initial de la PR : `289ef77674c0fd30c2d6a86bc23070baecf1ba2e`
- Commit des nouveaux tests HTTP : `7e18fe75c69573e1fb0e900cb7b2b10e89cb90c0`

La PR contient trois fichiers modifiés du CMS officiel :

1. `eclair/app/lib/Extensions.php` : routes POST publiques déclaratives, `HTTPS`, preuve CSRF, réponse `no-store`, type MIME texte, taille de corps déclarée limitée à 64 Kio, redirections locales `303`.
2. `docs/schemas/extension.schema.json` : possibilité d'annoncer la méthode POST dans le manifeste (avec refus côté noyau si la route est déclarée `cache:true`).
3. `tests/extensions.php` : tests natifs de validation d'un POST sans cache, rejet d'un POST avec cache, et rejet d'un POST sur chemin interne.

## Statut des preuves

- Les tests locaux de Member Directory (145 assertions PHP isolées) ainsi que les 20 tests Python du kit v1.2 ont réussi, mais **ces tests ne constituent pas des essais du noyau HTTP réel**.
- Un `git clone` direct échoue dans ce conteneur à cause de la résolution DNS. La PR a été déposée grâce au connecteur GitHub.
- La CI GitHub est la source faisant foi pour les tests du noyau officiel. Voir https://github.com/Jacckisback/eclair-cms/actions pour les résultats du commit de la PR.
- La PR ne contient pas Member Directory lui-même : ne pas confondre support POST et identité publique qualifiée.

## Conditions avant fusion

- Réussite de la matrice PHP du noyau, tests sur archive, validation des budgets de performance.
- Tests HTTP sur TLS, faux proxy, CSRF, cookies, absence de cache y compris `GET` privé et proxy CDN.
- Validation de l'extension avec `php tools/validate.php`, puis scénarios d'inscription et récupération email sur serveur réel.
- Audit indépendant contre énumération de comptes, brute-force concurrent, temporisation, réutilisation de jetons, fuites d'URL et erreurs SMTP.
- Examen des politiques d'accès et de suppression des données personnelles.

Ne pas déployer la PR en production. Ne pas fusionner sans revue.
