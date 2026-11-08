# Plan de validation — Quiz et attestations

## Modèle de données
Question, choix, correction, tentative, score, délai, attestation et vérification.

## Implémentation attendue
Versionner banque de questions; noter côté serveur; définir tentatives et temps; générer attestation signée/vérifiable sans PII publique.

## Tests à prévoir
1. Nominal : Tester triche, fin de session, validation du certificat.
2. Contrôle de refus : Soumettre deux fois une tentative ne doit pas générer deux certificats.
3. Invariant : Ne jamais envoyer corrigé ou réponse juste dans le HTML d’une épreuve active.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
