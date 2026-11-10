# Piano di validazione — Tag e tassonomie

## Modello di dati
Termine, tipo di tassonomia, contenuti collegati, indirizzo di archivio.

## Implementazione attesa
Inventariare le tassonomie esistenti, unire quelle che duplicano le categorie, proporre pagine di raggruppamento in GET per il resto e reindirizzare i vecchi archivi.

## Test da prevedere
1. Nominale: Convertire un insieme di tag in categorie o in pagine di raggruppamento e verificare i reindirizzamenti.
2. Controllo di rifiuto: Un vecchio archivio di tag eliminato reindirizza alla pagina più vicina, senza catena.
3. Invariante: Non generare centinaia di archivi poveri indicizzabili.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
