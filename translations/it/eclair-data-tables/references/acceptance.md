# Piano di validazione — Tabelle di dati

## Modello di dati
Tabella, intestazioni, righe, didascalia.

## Implementazione attesa
Usare il blocco tabella nativo, aggiungere didascalia e intestazioni, prevedere uno scorrimento orizzontale controllato.

## Test da prevedere
1. Nominale: Leggere la tabella su mobile e con lo screen reader.
2. Controllo di rifiuto: Una tabella larga non provoca lo scorrimento orizzontale dell'intera pagina.
3. Invariante: Nessun dato personale in una tabella pubblica senza consenso.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
