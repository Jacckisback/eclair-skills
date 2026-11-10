# Piano di validazione — Feed prodotti

## Modello di dati
Prodotto, prezzo, disponibilità, immagine, identificatori.

## Implementazione attesa
Completare le schede, controllare il feed prodotto dal core, dichiararlo nello strumento per i commercianti, correggere i rifiuti.

## Test da prevedere
1. Nominale: Validare il feed e confrontare tre prodotti con la rispettiva scheda.
2. Controllo di rifiuto: Un prodotto non disponibile non viene annunciato come disponibile.
3. Invariante: Prezzo e disponibilità del feed sono quelli della scheda pubblica.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
