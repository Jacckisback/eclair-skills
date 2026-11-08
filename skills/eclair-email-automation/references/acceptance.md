# Plan de validation — Emails transactionnels

## Modèle de données
Template, langue, consentement, destinataire, domaine, événement, livraison.

## Implémentation attendue
Préparer modèles texte/HTML, DKIM/SPF/DMARC et délivrabilité; distinguer transactionnel et marketing, journal sans secrets, désabonnement requis.

## Tests à prévoir
1. Nominal : Tester erreur SMTP, erreur d’adresse, reprise et expiration de token.
2. Contrôle de refus : Un échec SMTP ne marque pas un email comme livré ni ne bloque un compte définitivement.
3. Invariant : Ne pas envoyer token de récupération par URL non vérifiée; jamais de spam sans consentement.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
