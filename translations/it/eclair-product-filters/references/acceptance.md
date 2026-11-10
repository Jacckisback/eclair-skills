# Piano di validazione — Filtri e ordinamento del catalogo

## Modello di dati
Criterio, valore, combinazione, indirizzo filtrato.

## Implementazione attesa
Basarsi sui filtri per categoria nativi; aggiungere filtri lato browser su dati pubblici, con indirizzi canonici sotto controllo.

## Test da prevedere
1. Nominale: Filtrare e ordinare un catalogo di test su mobile.
2. Controllo di rifiuto: Una combinazione senza risultati mostra un messaggio, non una pagina vuota indicizzabile.
3. Invariante: Le combinazioni di filtri non creano un'infinità di pagine indicizzabili.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
