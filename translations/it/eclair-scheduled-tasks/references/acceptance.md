# Piano di validazione — Task pianificati

## Modello di dati
Task, frequenza, ultima esecuzione, risultato.

## Implementazione attesa
Dichiarare il task nel manifest (al massimo una volta all'ora), chiamare l'indirizzo segreto del core dallo scheduler del provider di hosting, registrare nei log.

## Test da prevedere
1. Nominale: Eseguire il task due volte di seguito e verificare un solo effetto.
2. Controllo di rifiuto: Una chiamata senza il token segreto non attiva nulla.
3. Invariante: L'indirizzo segreto dei task non viene mai pubblicato; ogni task è idempotente.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
