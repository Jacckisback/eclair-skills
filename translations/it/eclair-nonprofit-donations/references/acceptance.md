# Piano di validazione — Donazioni e associazioni

## Modello di dati
Causa, progetto, importo, link di donazione, ricevuta.

## Implementazione attesa
Presentare la missione e l'uso dei fondi, collegare i pulsanti di donazione a link del fornitore, demandare la gestione delle ricevute al fornitore o all'associazione.

## Test da prevedere
1. Nominale: Fare una donazione in modalità di test e seguire l'intero percorso.
2. Controllo di rifiuto: Un importo modificato nella pagina non cambia l'importo incassato.
3. Invariante: Nessuna promessa di vantaggio fiscale senza conferma dell'associazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
