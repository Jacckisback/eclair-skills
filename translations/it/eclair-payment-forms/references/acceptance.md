# Piano di validazione — Moduli di pagamento

## Modello di dati
Prestazione, importo, link di pagamento del fornitore.

## Implementazione attesa
Creare il link presso il fornitore di servizi di pagamento, mostrarlo su una pagina chiara con le condizioni, non archiviare nulla sul sito.

## Test da prevedere
1. Nominale: Pagare in modalità test e verificare ricevuta e pagina di ritorno.
2. Controllo di rifiuto: Un importo modificato lato browser non ha alcun effetto sull'importo incassato.
3. Invariante: Nessun dato bancario transita né viene archiviato sul sito.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
