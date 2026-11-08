# Revue de sécurité — Éclair Skills v2.0.0

*English summary at the end.*

Date : 8 novembre 2026. Périmètre : ce dépôt (57 skills, scripts, exemples, CI). Le noyau Éclair CMS n’est pas audité ici.

## 1. Ce qu’est un skill du point de vue de la sécurité

Un skill n’est pas du code exécuté par votre site : c’est **un texte d’instructions lu par un agent IA**, qui agit ensuite avec **vos droits** (fichiers, terminal, Git, parfois accès réseau). Le risque principal n’est donc pas « un bug PHP dans le skill », mais :

- **un skill modifié** qui pousse l’agent à faire autre chose que prévu (exfiltrer des secrets, ajouter une porte dérobée, désactiver une vérification) : c’est une attaque de la chaîne d’approvisionnement par injection d’instructions ;
- **un skill sincère mais mal suivi** : l’agent produit quand même du code vulnérable.

## 2. Constats et mesures

| # | Gravité | Constat | Mesure |
|---|---|---|---|
| 1 | **Critique** | La clé privée `ECLAIR_SIGNING_KEY` présente dans l’environnement cloud de l’agent est **la clé du mainteneur d’Éclair CMS** : sa clé publique est celle de `eclair/app/lib/Update.php` (`KEY`). Quiconque peut lire cet environnement (une session d’agent, une instruction malveillante cachée dans une issue, une page web ou un fichier) peut signer une **fausse mise à jour du CMS** que tous les sites Éclair accepteraient. | **À faire par le mainteneur** : retirer `ECLAIR_SIGNING_KEY` de l’environnement cloud et signer uniquement en local, idéalement sur une machine dédiée ou avec une clé hors ligne. Voir § 4. |
| 2 | Élevée | Sans signature, rien ne prouvait qu’une copie des skills (clone, ZIP, fork) était l’originale. | **Fait** : `SIGNATURE.json` (Ed25519, clé du mainteneur, contexte `eclair-skills/release/1:`) couvre `SHA256SUMS.json`, qui couvre chaque fichier. `php scripts/verify_signature.php` vérifie la signature avec la clé publique **figée dans le script**, chaque empreinte, l’absence de fichier ajouté et de lien symbolique. La CI exige une signature valide sur `main`. |
| 3 | Élevée | Réutiliser la clé du CMS pour les skills pourrait permettre de rejouer une signature d’un usage dans l’autre. | **Fait et vérifié** : le message signé commence par `eclair-skills/release/1:`. Le système de mise à jour exige `eclair-cms/annonce/2:` (format 2) ou un JSON brut (format 1) : une signature de skills n’y est jamais valide, et inversement. Une clé dédiée aux skills reste préférable (§ 4). |
| 4 | Moyenne | Une modification directe de `main` (compte compromis, erreur) serait publiée sans relecture. | **À faire dans GitHub** : protéger `main` (PR obligatoire, CI verte obligatoire, pas de force-push), activer l’authentification à deux facteurs et les commits signés. |
| 5 | Moyenne | `shutil.copytree` copierait le *contenu* d’un lien symbolique placé dans un skill (par exemple vers `~/.ssh`). | **Fait** : `check_release.py` et `verify_signature.php` refusent tout lien symbolique. Toujours lancer `verify_signature.php` avant `install_skills.py`. |
| 6 | Moyenne | Actions GitHub référencées par étiquette mobile (`@v4`) : un tag déplacé chez un tiers changerait le code exécuté par la CI. | **Fait** : les trois actions sont figées par SHA de commit ; permissions du workflow en lecture seule ; aucun secret dans la CI. |
| 7 | Moyenne | Un agent qui suit un skill peut tout de même écrire du code vulnérable. | Les skills imposent CSRF, permissions, échappement, absence de PII en cache et tests de refus, mais **ce n’est pas une garantie**. Faire relire par un humain, utiliser `eclair-security-audit` et `eclair-test-suite`, ne jamais déployer automatiquement. |
| 8 | Moyenne | `examples/extensions/member-directory` et `core-patch/` (qui modifie le noyau) sont expérimentaux. | Ne pas les déployer en production. Ils restent signalés comme tels partout dans la documentation. |
| 9 | Faible | L’agent qui utilise les skills lit aussi du contenu non fiable (issues, pages web, fichiers clients). | Donner à l’agent le minimum de droits : pas de secrets de production dans son environnement, pas d’accès en écriture à la production, relecture humaine avant publication. |

Contrôles passés le 8/11/2026 : recherche de secrets (aucune clé, aucun jeton, aucune donnée client dans le dépôt), refus des liens symboliques, validation structurelle des 57 skills, tests Python (26) et PHP isolés (59 + 28 + 58), empreintes SHA-256 de tous les fichiers.

## 3. Ce que la signature prouve, et ce qu’elle ne prouve pas

- ✅ **Prouve** que les fichiers sont exactement ceux signés par le détenteur de la clé du mainteneur, sans ajout, suppression ni modification.
- ❌ **Ne prouve pas** que le contenu est sans danger : elle prouve l’origine, pas la qualité. La relecture reste nécessaire.
- ❌ **Ne protège plus rien si la clé fuit** : d’où le constat n° 1.

## 4. Gestion de la clé : recommandations

1. **Retirer `ECLAIR_SIGNING_KEY` de l’environnement cloud** (paramètres de l’environnement, section des variables). Signer sur votre ordinateur :
   ```bash
   python3 scripts/check_release.py --write
   ECLAIR_SIGNING_KEY="$(cat /chemin/hors-depot/eclair.key)" php scripts/sign_release.php
   php scripts/verify_signature.php
   ```
2. **Créer à terme une clé dédiée aux skills** pour que la clé du CMS ne serve qu’aux mises à jour du CMS. Il suffit de changer la constante `PUBLIC_KEY` de `scripts/verify_signature.php` dans une version signée par l’ancienne clé.
3. **Si une fuite est possible** (la clé a séjourné dans un environnement partagé) : envisager une rotation de la clé du CMS, c’est-à-dire publier une version du CMS signée par l’ancienne clé qui embarque la nouvelle clé publique, puis ne plus jamais utiliser l’ancienne.
4. Garder une sauvegarde chiffrée de la clé hors ligne ; ne jamais la commiter, la coller dans un chat ou la mettre dans une CI publique.

## 5. Procédure pour toute nouvelle version

1. Modifier, puis `python3 scripts/build_readmes.py` si le catalogue ou les textes changent.
2. `python3 scripts/check_release.py --write`, puis signer avec `sign_release.php`.
3. `php scripts/verify_signature.php` et tous les tests ; ouvrir une PR ; fusionner quand la CI est verte.

---

## English summary

A skill is instructions read by an AI agent acting with your rights; the main risk is a **tampered skill** steering the agent (prompt-injection supply-chain attack). Done: every release is signed (Ed25519, maintainer key, domain-separated context `eclair-skills/release/1:` that can never be replayed as an Éclair CMS update), `php scripts/verify_signature.php` checks the pinned key, every SHA-256, extra files and symlinks; CI requires a valid signature on `main`; GitHub Actions are pinned by commit SHA. **Critical:** the signing key found in the cloud agent environment is the Éclair CMS update key; the maintainer should remove it from that environment, sign locally, consider a dedicated skills key, and rotate the CMS key if exposure is possible. A signature proves origin and integrity, not safety: human review is still required.
