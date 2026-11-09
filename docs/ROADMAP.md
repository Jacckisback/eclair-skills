# Feuille de route des skills — de l’agent au site métier

## Les quatre niveaux de maturité

1. **Workflow** : `SKILL.md` permet de concevoir, vérifier les interfaces et éviter les erreurs. Tous les skills livrés ont ce niveau.
2. **Paquet v2 natif** : `extension.json` valide, code GET/read-only ou admin protégé, `tools/validate.php` + tests natifs.
3. **Moteurs métiers** : comptes, POST, transactions, webhooks, audit sécurité, performance, sauvegarde/restauration, CI.
4. **Application en production** : déploiement limité, monitoring, restauration vérifiée, supervision, conformité légale.

## Suites de référence à construire

- **Commerce Pro (10 skills)** : réaliser d’abord le catalogue GET, puis données transactionnelles, puis commande et PSP sandbox, ensuite vrais paiements uniquement après audit.
- **LMS (7)** : catalogue de cours, autorisations apprenant, inscription/progression idempotente, évaluations, analytics privés.
- **Forum (6)** : catégories GET, authentification, publication privée, anti-spam/modération, notifications, recherche permissions.
- **Applications métiers (8)** : démos publiques puis mutations sécurisées et concurrence.
- **Design (7)** : thème natif v2 et tests accessibilité/performance (Éclair Design réutilisé sans duplication).
- **SEO/GEO/migration (5)** : priorité à import WordPress natif, comparatif URL/redirects, schémas réellement supportés.
- **Intégrations (6)** : webhooks, email, API/CRM, aide IA, observabilité, contract tests.

## Cinq gates impératives pour activer une application commerciale

1. Compatibilité prouvée sur la version exacte du CMS, y compris PHP 8.1–8.5 supportés, Apache/Nginx et archive réelle.
2. Authentification et isolation des données privées testées en conditions réseau réelles, y compris sessions et réinitialisation.
3. Stockage et transaction : crash/reprise/concurrence; paiement signé, déduplication et réconciliation pour toute vente.
4. Audit sécurité autonome, conformité applicable et mise en production progressive sur serveur de test.
5. Budget de performance et SEO/GEO sans régression sur les pages vitrines et le chemin cache.
