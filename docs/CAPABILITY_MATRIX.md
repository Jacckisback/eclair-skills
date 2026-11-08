# Éclair CMS 2.0.x : ce qui fonctionne et ce qui reste à construire

| Fonction | Contrat 2.0 actuel | État du kit |
|---|---|---|
| Pages publiques GET statiques, SEO/GEO natif | Oui | Exemple installable en principe (validation native requise) |
| Blocs custom d’extension et thèmes | Oui | Skills design disponibles |
| Administration GET/POST, CSRF/droits du CMS | Oui | Construction de modules admin possible |
| Tâches d’extension (≥ 3 600 secondes) | Oui | Skills intégration disponibles |
| Inscription/connexion publiques, POST | Non sur `main` | PR #19 passée en CI mais brouillon, non fusionnée |
| Paiement, panier, commandes transactionnelles | Non | Spécifications et tests de conception, pas de boutique live |
| Stockage SQL transactionnel opt-in et migrations | Non natif comme contrat général | RFC/skills, ne pas importer ancien prototype v0.x |
| Webhook signé + outbox persistante | Non comme système extensible standard | RFC/skills, pas de promesse de livraison garantie |
| LMS privé avec suivi | Non | Workflows uniquement, dépendances explicitées |
| Forum avec écriture/modération | Non | Workflows uniquement, dépendances explicitées |
| Import WordPress et préservation d’URLs | Fonction native disponible | Skills SEO/migration exploitables |
| JSON-LD personnalisé par extension | API générale pas ouverte | RFC à prévoir ; ne pas injecter du code pour contourner |

**PR n°19 :** https://github.com/Jacckisback/eclair-cms/pull/19 (en brouillon à la vérification de ce kit). **CI :** résultats sur la branche, indépendants des tests Member Directory; aucun usage prod permis sans sécurité, HTTPS et validation métier.
