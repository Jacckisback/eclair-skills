> **Mise à jour v1.1.0 — prototype expérimental.** Les handlers GET/POST de connexion et de déconnexion existent désormais dans `member-directory` **mais ne fonctionnent pas dans Éclair 2.0 officiel non patché**. Le patch noyau proposé est limité à une branche de développement. Les comptes sont toujours provisionnés par administrateur et activés uniquement au moyen d'une preuve d'email délivrée par un canal de confiance (pas de parcours public d'inscription ou d'email implémenté). Les tests PHP sont isolés, sans tests TLS/HTTP de bout en bout.

---

# Member Directory : notes de sécurité et limites

## Historique v1.0 : garantie du prototype admin-only
- Une extension native sous `site/extensions/member-directory/` sans aucune route publique.
- Les opérations administrateur `create` et `disable` requièrent `users` + CSRF ; elles ne doivent être appelées que via le contrôleur d'administration natif.
- `MemberAccounts` crée des comptes `pending`, génère un mot de passe temporaire aléatoire jamais affiché, interdit d'utiliser `admin`/`editor` comme rôle membre et limite à 1000 les comptes sur fichiers.
- Les sessions sont opaques, hachées en stockage et révocables par changement d'époque, mais ne sont PAS câblées à un login public.
- `MemberPermissions` applique le refus par défaut et contrôle la propriété des ressources avec un jeton validé.

## Ce qui n'est PAS garanti
- Un **primitif** de preuve email (jeton à usage unique/30 min haché au repos) est fourni, MAIS aucune délivrance d'email ni route de confirmation publique n'est exposée. Pas de récupération de mot de passe ni de flux d'invitation complet.
- Pas de limitation de tentatives sur un endpoint public (puisqu'il n'existe pas) ; aucune garantie de durabilité transactionnelle multi-fichiers.
- Pas de tests avec l'authentique pile HTTP d'Éclair 2.0, de tests sur serveurs Apache/Nginx, ni de benchmark Lighthouse.
- Pas d'audit indépendant ni de certification de sécurité. Ne pas installer en production.

## Scénarios de menaces avant ouverture publique
1. Vol ou fixation de session : cookie TLS, rotation au login, révocation, logout et expiration.
2. Énumération des comptes : réponses indifférenciées, limitation des tentatives, timings similaires.
3. Escalade de privilège : aucun rôle admin, droits par capacité et par objet.
4. Fuite via cache/CDN : réponses membre toujours `private, no-store` et exclusives du chemin rapide de cache.
5. CSRF/login CSRF : rejet des POST inter-origines et jetons CSRF attachés à session valide.
6. Réinitialisation de mot de passe : preuve email à usage unique, durée courte, révocation des sessions.
7. Modification concurrente : transactions et unicité d'email assurées par stockage adapté avant montée en charge.
8. Protection des données : consentement, effacement, durée de conservation et minimisation RGPD à définir avant tout déploiement.

## Pour les agents IA
Lire `docs/MEMBER_IDENTITY_RFC.md`, vérifier `docs/EXTENSION-CONTRACT.md` du checkout officiel courant, utiliser son validateur et arrêter avant toute installation production. Les anciens prototypes v0.8 ne doivent pas remplacer les composants du noyau 2.0.
