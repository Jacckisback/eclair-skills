# Piano di validazione — Ricerca nel sito

## Modello di dati
Indice dei contenuti pubblicati, titolo, estratto, indirizzo.

## Implementazione attesa
Generare un indice statico dei contenuti pubblici tramite attività pianificata, servirlo in GET memorizzabile in cache e cercare lato browser con una pagina di ripiego senza JavaScript.

## Test da prevedere
1. Nominale: Cercare un termine presente, assente, accentato e verificare il tempo di risposta.
2. Controllo di rifiuto: Una bozza o una pagina privata non compare mai nell'indice.
3. Invariante: L'indice contiene soltanto contenuti pubblici ; nessuna richiesta di un visitatore viene registrata nei log con la sua identità.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
