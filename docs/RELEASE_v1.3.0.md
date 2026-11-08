# Notes de version v1.3.0 — validation native engagée

Version de consolidation : aucune nouvelle interface publique de Member Directory n'est revendiquée.

La PR brouillon #19 dans le dépôt officiel Éclair 2.0 apporte un premier changement natif du contrat d'extensions pour préparer l'authentification publique. Ce package contient les huit skills et l'extension prototype déjà existants en v1.2, plus un dossier de suivi d'intégration. Le script de patch local `core-patch/apply_public_post.py` hérité de v1.2 doit être traité comme une **ancienne proposition** ; la PR #19, dont le code inclut d'autres protections, est la référence pour la v1.3.

Ne pas utiliser les exemples sur un site public ou avec des comptes clients réels tant que la validation HTTP, les tests CMS complets, l'audit SMTP et la revue de sécurité ne sont pas terminés.
