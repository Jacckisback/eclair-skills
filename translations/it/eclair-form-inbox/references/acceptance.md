# Piano di validazione — Messaggi ricevuti

## Modello di dati
Messaggio, stato, risposta, durata di conservazione.

## Implementazione attesa
Definire chi legge e risponde, entro quale termine, per quanto tempo i messaggi vengono conservati, come vengono eliminati.

## Test da prevedere
1. Nominale: Gestire un messaggio dalla ricezione all'archiviazione.
2. Controllo di rifiuto: Un account senza il permesso Messages non accede ad alcun messaggio.
3. Invariante: Durata di conservazione limitata e permesso di accesso ristretto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
