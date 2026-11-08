# Release notes — Éclair Skills v1.0.0 (prototype)

Version cible : Éclair CMS 2.0.0. Ne modifie aucun fichier du noyau officiel.

## Livré
- Les huit skills initiaux, avec références autonomes mises à jour.
- L'exemple d'extension native `member-directory` (admin seulement) : gestion minimale des comptes `pending`, désactivation, sessions de membre et RBAC/ownership de référence.
- Jetons de preuve d'email à usage unique, 30 minutes, hachés au stockage ; **envoi d'email et endpoint public non implémentés**.
- Routes d'administration protégées par le droit `users` et le CSRF natif, vérifié aussi par les handlers.
- Test PHP isolé et tests de manifeste/empreintes/tamper offline.

## Ce qui manque pour le public
- API POST publique native et route privée hors du cache statique ; aucun contournement par GET.
- Livraison de la preuve email, limitation de tentatives, reset, cookies et flux HTTP testés de bout en bout.
- Stockage SQL transactionnel testé pour les charges commerce/LMS/forum.
- Validation complète avec l'authentique noyau Éclair 2.0 (`tools/validate.php`, `tests/run.php`, `tools/measure.php`).

## Statut
**Laboratoire uniquement**, ne pas installer avec des données réelles de clients/élèves. Une extension PHP n'est pas un bac à sable : activation manuelle par un opérateur de confiance après vérification.
