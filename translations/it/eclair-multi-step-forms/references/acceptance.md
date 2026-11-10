# Piano di validazione — Moduli a più passaggi

## Modello di dati
Passaggio, campi, validazione, bozza di risposta.

## Implementazione attesa
Suddividere per tema, validare lato server a ogni passaggio, prevedere ripresa e riepilogo prima dell'invio.

## Test da prevedere
1. Nominale: Compilare, tornare indietro, correggere e inviare.
2. Controllo di rifiuto: Un passaggio non valido blocca il seguito e nessun dato incompleto viene trasmesso.
3. Invariante: Nessun dato parziale viene conservato senza che la persona ne sia informata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
