# Piano di validazione — Link interni

## Modello di dati
Pagina sorgente, pagina di destinazione, anchor text, pagine orfane.

## Implementazione attesa
Mappare i link, individuare le pagine orfane, aggiungere link utili con anchor text descrittivi.

## Test da prevedere
1. Nominale: Verificare che ogni pagina importante riceva almeno un link interno.
2. Controllo di rifiuto: Nessun link interno punta a un reindirizzamento o a un errore.
3. Invariante: Nessun link viene aggiunto automaticamente senza rilettura del contesto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
