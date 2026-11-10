# Piano di validazione — Titoli e meta description

## Modello di dati
Titolo, meta description, espressione di destinazione, anteprima del risultato.

## Implementazione attesa
Redigere per ogni pagina un titolo e una descrizione unici, servirsi del punteggio in tempo reale dell'editor senza trattarlo come un obiettivo.

## Test da prevedere
1. Nominale: Controllare unicità e lunghezza su tutte le pagine.
2. Controllo di rifiuto: Due pagine pubblicate non hanno lo stesso titolo.
3. Invariante: Nessuna promessa di posizione ; nessun keyword stuffing.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
