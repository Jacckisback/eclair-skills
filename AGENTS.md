# Éclair Skills v2.0.0 — consignes pour les agents

- **Découvrir** version/contrats (`GET /<admin>/api/capabilities` si autorisé); consulter `catalog.json` et le skill déclenché.
- **Préserver le noyau** : ne toucher ni `app/`, `assets/`, `index.php`, updater, authentification ou SEO intégré dans une tâche de création de site. Les modifications structurelles demandent une PR spécifique et tests complets.
- **Créer dans `site/`** : thème natif (`site/themes`) ou fonction (`site/extensions`) avec manifeste `eclair-extension/1` et validateur officiel.
- **Respecter la limite v2** : GET public uniquement sur `main`, GET/POST administration protégés; route POST publique expérimentale PR #19 non fusionnée. Impossible de livrer une vraie commande/LMS/Forum en écriture publique sans nouvelle interface qualifiée.
- **Garder le chemin rapide** : aucune donnée personnelle ou résultat de session dans un cache partagé; aucune déclaration non mesurée de Lighthouse 100 ni de référencement garanti.
- **Sécurité** : CSRF, TLS, permissions objet, échappement, rate limits, secrets privés; paiements avec vérification prestataire et traitement idempotent.
- **Valider** : `tools/validate.php`, `tests/run.php`, `tools/measure.php --check`, puis tests HTTP/SMTP et sécurité si le cas l'exige.
- **Installer et publier** : l'agent prépare, une personne autorisée vérifie; jamais de déploiement, publication ou changement de contrats implicites.
- **Conserver les données** : migrations idempotentes; désactiver ne supprime pas les données; prévoir sauvegarde et restauration.
- **Ne pas confondre** : 57 skills = instructions pour agent, pas 57 plugins PHP. Le catalogue-vitrine est un exemple fonctionnel GET-only; Member Directory est expérimental.
