# Piano di validazione — Architettura Forum

## Modello di dati
Spazio, categoria, argomento, messaggio, autore, ruolo, segnalazione, blocco.

## Implementazione attesa
Separare argomenti indicizzabili e privati; prevedere paginazione stabile, permessi per oggetto, quote e moderazione; predisporre un motore di ricerca limitato.

## Test da prevedere
1. Nominale: Testare visitatore, membro, moderatore e account sospeso.
2. Controllo di rifiuto: Argomento privato inesistente per un membro non autorizzato, anche tramite ricerca.
3. Invariante: Nessuna scrittura anonima senza anti-spam, CSRF e limitazione della frequenza; mai HTML arbitrario eseguito.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
