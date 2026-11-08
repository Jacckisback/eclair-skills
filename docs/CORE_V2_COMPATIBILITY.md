# Compatibilité : des prototypes 1.14.2 à l'architecture native Éclair 2.0.0

Instantané vérifié sur `Jacckisback/eclair-cms` le 8 novembre 2026, commit `0beb440655090fbd9c3b58e8c56dca7ddbb2106e` (recontrôler avant utilisation). Le noyau officiel s'annonce `ECLAIR_VERSION = 2.0.0`.

| Capacité | v0.8 expérimental (1.14.2) | Éclair 2.0 natif | Décision |
|---|---|---|---|
| Routage des fonctions | ExtensionBridge/RouteRegistry | `Extensions::route()`, `extension.json`, `routes.public/admin` | Utiliser natif ; ne pas porter l'ancien routeur |
| Activation, dépendances, migration | ModuleCatalog CLI | `Extensions`, `AdminExtensions`, `Packages`, `Migrations` | Utiliser natif |
| Gestion du cache | CacheFence | Cache statique + invalidation à activation + `routes.public[].cache` | Valider les scénarios, pas de double cache fence |
| Stockage | Store natif + PDO pilote | `Store` natif, données `data/ext/<id>` | Natif pour contenu ; SQL optionnel à qualifier |
| Identité et permissions | MemberAccounts/MembersSessions pilote | `Auth/Users` **administration seulement** | Manque identité publique ; RFC distincte |
| Événements métiers | EventBus, ServiceRegistry, DurableOutbox pilote | Pas de contrat public de bus/outbox versionné en 2.0 | RFC et tests avant modules transactionnels |
| SEO/GEO extensions | Projet | En-tête SEO standard ; contributions personnalisées non ouvertes | RFC, ne pas doubler les canonicals |
| Suite de tests | Contrats isolés | `php tests/run.php` ; `tools/measure.php --check` ; validate.php | Utiliser tests natifs |

## Garde-fou de migration

Aucun des scripts `apply_to_core.py`, `upgrade_from_v0*.py` du kit expérimental 1.14.2 ne doit viser le dépôt 2.0.0. Les anciens ZIP restent une archive de recherche. Une fonctionnalité métier v2 doit être un paquet `site/extensions/<id>/` conforme au schéma officiel et révisé indépendamment du noyau.

## Domaines réellement manquants

- Endpoints publics POST avec contrôle d'accès utilisateur (commerce et LMS).
- Modèle d'identité membre distinct des comptes admin.
- Stockage transactionnel facultatif et son cycle de maintenance.
- Événements durables, reçus idempotents, reprise et dead-letter.
- Types de contenus métiers et contributions SEO structurées par fonction, sans casser le balisage natif.
- CSP configurable de manière sûre pour une extension qui en aurait véritablement besoin.

Ces sujets appellent des PR/RFC dédiées et des tests compatibles avec le contrat natif 2.0 ; ne pas les implémenter à l'aveugle dans l'ancien adaptateur.
