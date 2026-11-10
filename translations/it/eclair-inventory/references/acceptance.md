# Piano di validazione — Stock e prenotazioni

## Modello di dati
SKU, magazzino, stock fisico, riservato, disponibile, movimenti immutabili.

## Implementazione attesa
Progettare i movimenti di entrata/uscita; bloccare la prenotazione con un lock; gestire scadenza e compensazione; tracciare tutte le correzioni manuali.

## Test da prevedere
1. Nominale: Testare acquisti simultanei dell'ultimo esemplare e rilascio dopo la scadenza.
2. Controllo di rifiuto: Due acquirenti non possono riservare lo stesso ultimo pezzo a stock.
3. Invariante: La lettura memorizzabile in cache della disponibilità è informativa; ogni vendita rilegge lo stock in una transazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
