# Plan de validation — Quiz et attestations

## Modèle de données
Question, choix, correction, tentative, score, délai, attestation et vérification.

## Mise en œuvre attendue
Versionner banque de questions; noter côté serveur; définir tentatives et temps; générer attestation signée/vérifiable sans PII publique.

## Tests à prévoir
1. Nominal : Tester triche, fin de session, validation du certificat.
2. Contrôle de refus : Soumettre deux fois une tentative ne doit pas générer deux certificats.
3. Invariant : Ne jamais envoyer corrigé ou réponse juste dans le HTML d’une épreuve active.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
