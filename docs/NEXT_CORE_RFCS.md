# Feuille de route vers Éclair Commerce, LMS et Forum (noyau 2.0)

## RFC-1 — Identité publique et requêtes POST

**Manque natif** : `eclair-extension/1` sait déclarer des GET publics et des routes d’administration protégées ; il ne fournit pas d'identité publique client/élève/modérateur ni de POST public métier.

- Identités séparées des utilisateurs admin, politique de mot de passe, vérification d'email, reset à usage unique, révocation des sessions, limitation des tentatives, protection des données.
- API d'extension pour routes publiques dynamiques avec `GET/POST`, autorisation propre au membre et protections CSRF/Origin ; vérification d'accès par objet.
- Cache partagé interdit pour toute page membre/personnalisée ; canonical/noindex cohérents.
- Tests : IDOR/BOLA, faux jetons, modification de rôle, session fixée/révoquée, refus par défaut, GET cacheable restant inchangé.

## RFC-2 — Stockage transactionnel facultatif

- Adapter un connecteur PDO SQL séparé et optionnel, sans imposer de DB aux sites vitrines ; permettre SQLite et MySQL uniquement avec transactions et schémas explicitement pris en charge.
- Éviter de confondre `Store::locked` avec une transaction multi-enregistrement.
- Composer migrations, verrous, backup cohérent et restauration à froid avec le cycle de vie des extensions natives.
- Tests SQL PHP réels (pdo_sqlite + pdo_mysql selon moteurs promis), concurrence, rollback, corruption, upgrade/restore. Le pilote v0.8 est une référence de recherche, pas un composant v2 activable.

## RFC-3 — Bus d'événements et outbox durables

- Déclarer capacités productrices/consommatrices versionnées, enregistrer événements dans la même transaction SQL que le changement métier.
- Worker CLI privé, baux, retries, dead-letter, redrive contrôlé, reçus transactionnels par consommateur.
- Semantique *at least once*, idempotence obligatoire ; actions externes exigent une stratégie spécifique.
- Tests : interruption avant/après commit, doublons, concurrence de workers, replay, erreurs de webhook, redémarrage.

## RFC-4 — SEO et types métier (après socle transactionnel)

- Contributions Schema.org `Product`, `Course`, `DiscussionForumPosting` produites sans double canonical ni duplication JSON-LD.
- Pages/révisions personnalisées, sitemap et flux pensés dès le départ pour coexister avec le routeur natif.
- Tests : 404, canonical, noindex privé, hreflang si multilingue, sitemap, performances.

**Ordre conseillé :** RFC-1 → RFC-2 → RFC-3, puis Commerce/LMS/Forum sur contrats communs, et RFC-4 par besoin SEO. Chaque RFC doit proposer des modifications minimales du noyau, une stratégie de migration 2.x et un budget de performance, et ne doit jamais écraser les `site/extensions/` existants.
