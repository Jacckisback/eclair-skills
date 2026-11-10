# Piano di validazione — Tipi di contenuto personalizzati

## Modello di dati
Scheda di settore, campi, elenco, indirizzo, stato.

## Implementazione attesa
Scegliere tra pagine con blocchi dedicati ed estensione con archiviazione propria e route GET, fissare gli indirizzi, prevedere elenco e scheda.

## Test da prevedere
1. Nominale: Creare un tipo di scheda tramite estensione, con elenco e dettaglio in GET, poi validare il pacchetto.
2. Controllo di rifiuto: Una scheda non pubblicata non viene servita né nell'elenco né al suo indirizzo diretto.
3. Invariante: Non scrivere mai nei file di contenuto del core da un'estensione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
