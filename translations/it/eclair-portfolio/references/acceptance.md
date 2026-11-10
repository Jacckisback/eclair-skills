# Piano di validazione — Portfolio e lavori realizzati

## Modello di dati
Lavoro realizzato, cliente, contesto, risultato, immagini.

## Implementazione attesa
Redigere ogni lavoro come problema, soluzione, risultato, con immagini leggere e consenso del cliente.

## Test da prevedere
1. Nominale: Scorrere elenco e dettaglio su mobile.
2. Controllo di rifiuto: Un lavoro senza consenso registrato resta in bozza.
3. Invariante: Nessun cliente, cifra o risultato pubblicato senza consenso.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
