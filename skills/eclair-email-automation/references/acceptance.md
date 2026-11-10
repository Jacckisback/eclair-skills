# Plan de validation — Emails transactionnels

## Modèle de données
Template, langue, consentement, destinataire, domaine, événement, livraison.

## Mise en œuvre attendue
Préparer modèles texte/HTML, DKIM/SPF/DMARC et délivrabilité; distinguer transactionnel et marketing, journal sans secrets, désabonnement requis.

## Tests à prévoir
1. Nominal : Tester erreur SMTP, erreur d’adresse, reprise et expiration de token.
2. Contrôle de refus : Un échec SMTP ne marque pas un email comme livré ni ne bloque un compte définitivement.
3. Invariant : Ne pas envoyer token de récupération par URL non vérifiée; jamais de spam sans consentement.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
