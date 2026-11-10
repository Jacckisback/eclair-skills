# Piano di validazione — SEO locale

## Modello di dati
Nome, indirizzo, telefono, orari, zona servita.

## Implementazione attesa
Inserire i recapiti esatti nelle impostazioni, verificare il markup di attività locale prodotto dal core, allineare scheda dell'attività e sito.

## Test da prevedere
1. Nominale: Confrontare i recapiti del sito, del markup e della scheda dell'attività.
2. Controllo di rifiuto: Orari non confermati non vengono pubblicati.
3. Invariante: Nessun indirizzo, recensione o zona di intervento inventati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
