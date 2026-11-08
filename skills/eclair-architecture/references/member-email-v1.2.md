# Référence technique — Member Directory v0.3.0 (Éclair v2.0.0, contrat POST expérimental)

## Parcours disponibles (tous cache:false)

| Méthode | Route | Rôle |
|---|---|---|
| GET/POST | `/membres/connexion` | Formulaire / connexion d'un compte actif |
| GET | `/membres/espace` | Profil privé propre au jeton de session |
| POST | `/membres/deconnexion` | Déconnexion avec CSRF propre à la session |
| GET/POST | `/membres/inscription` | Email d'invitation, seulement si `registration_enabled=true` |
| GET/POST | `/membres/verification` | Choisir le mot de passe avec preuve email unique |
| GET/POST | `/membres/recuperation` | Demander un email de récupération si `recovery_enabled=true` |
| GET/POST | `/membres/reinitialisation` | Remplacer le mot de passe avec preuve unique |

## Mécanismes

- Pas de compte CMS/`Auth::can` pour les clients. Les profils `member` ne contiennent jamais de rôles `admin` ou `editor`.
- `MemberAccounts::provision` exige un mot de passe provisoire aléatoire et crée un compte `pending`. Le lien email demande à la personne de choisir son propre mot de passe. Le jeton de vérification expire en 30 minutes et un reçu ne s'utilise qu'une fois.
- `MemberAccounts::issueReset` délivre uniquement pour un membre `active`, puis `confirmReset` effectue la mutation sous verrou et incrémente `epoch`. Tous les anciens jetons de session deviennent invalides.
- `Mail::send` (service Éclair) est utilisé, mais n'est pas un accusé de livraison. Ne promettre aucun succès de livraison à l'utilisateur.
- Pour envoyer un email, l'URL canonique configurée doit être HTTPS et vérifiée. Le domaine de la requête HTTP est exclu du lien de récupération.
- Les pages GET n'effectuent aucun traitement métier ; le POST exige HTTPS et `Security::checkFormToken`, le patch de noyau vérifiant lui aussi ces conditions.
- Limiteurs par réseau / email, messages génériques sur les demandes, preuves validées deux fois (préflight avant le hash, puis sous verrou de stockage).
- Aucune ressource personnelle ne passe dans le cache statique public. Les liens à jeton doivent être exclus des journaux et toute page externe chargée depuis les formulaires de confirmation.

## Limites explicites

- Un compte en attente dont l'email est accepté par le transport mais jamais reçu nécessite un parcours de nouvelle invitation/assistance, non fourni ici.
- Les messages génériques ne suppriment pas totalement la possibilité d'inférer l'existence d'un compte par le délai d'exécution.
- Les jetons d'email en URL peuvent apparaître dans l'historique navigateur ou des logs : audit de l'infrastructure obligatoire.
- Le prototype `Store` est limité à 1 000 membres et n'est pas une base relationnelle transactionnelle multi-fichiers.
- Le contrat `eclair-extension/1` officiel n'autorise **pas** POST public sans patch. Toute installation sur un site réel attend sa validation.
