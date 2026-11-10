# Piano di validazione — API pubblica in lettura

## Modello di dati
Risorsa, campi pubblici, paginazione, versione.

## Implementazione attesa
Dichiarare route GET memorizzabili in cache che restituiscono JSON limitato e versionato; documentare che la scrittura non è aperta.

## Test da prevedere
1. Nominale: Leggere elenco e dettaglio, paginazione e caso vuoto.
2. Controllo di rifiuto: Un contenuto non pubblicato non viene restituito da alcuna route.
3. Invariante: Vengono esposti soltanto contenuti già pubblici; nessun identificativo interno sensibile.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
