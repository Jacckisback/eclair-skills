# Piano di validazione — Moduli e mini-CRM

## Modello di dati
Modulo, campo, consenso, contatto, origine, ticket e stato.

## Implementazione attesa
Definire finalità e durata di conservazione per ogni modulo; convalidare i dati lato server; proteggere dallo spam; isolare i file e il permesso di lettura.

## Test da prevedere
1. Nominale: Testare spam, allegato, duplicato ed eliminazione GDPR.
2. Controllo di rifiuto: Un utente senza permesso non può esportare la base dei contatti.
3. Invariante: Un modulo pubblico non deve consentire l'injection nelle email né far comparire i dati nella cache.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
