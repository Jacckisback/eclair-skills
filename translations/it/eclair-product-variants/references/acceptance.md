# Piano di validazione — Varianti e attributi

## Modello di dati
Prodotto genitore, varianti con SKU univoco, combinazioni di attributi, prezzo/stock propri, media e stato.

## Implementazione attesa
Definire il numero massimo di combinazioni; garantire l'unicità degli SKU; proiettare le varianti nella resa GET; predisporre una selezione validata dal server al momento del checkout.

## Test da prevedere
1. Nominale: Testare varianti assenti, esaurite e disattivate.
2. Controllo di rifiuto: Due combinazioni creano lo stesso SKU => rifiuto esplicito prima della pubblicazione.
3. Invariante: Non accettare mai come dati affidabili prezzo, peso o stock inviati dal browser.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
