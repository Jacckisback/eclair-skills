# Plan de validation — Modération et signalements

## Modèle de données
Signalement, motif, élément visé, décision, modérateur, audit.

## Implémentation attendue
Prévoir file de traitement, signalements abusifs, seuils/quotas, rollback et motifs; tracer décisions et restreindre pouvoirs par rôle.

## Tests à prévoir
1. Nominal : Tester modérateur sans droit global, utilisateur suspendu et appel.
2. Contrôle de refus : Un modérateur d’une catégorie ne peut pas voir les signalements privés d’une autre.
3. Invariant : Aucune suppression définitive automatique par signalement sans contrôle et preuves.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
