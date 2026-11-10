# Piano di validazione — Menu di navigazione

## Modello di dati
Menu, voce, ordine, destinazione, posizione.

## Implementazione attesa
Limitare il menu principale ai percorsi essenziali, collocare il resto nel piè di pagina, testare tastiera e mobile.

## Test da prevedere
1. Nominale: Comporre i menu e percorrerli da tastiera e su mobile.
2. Controllo di rifiuto: Una pagina non più pubblicata scompare dal menu o viene segnalata, mai servita in 404 dalla navigazione.
3. Invariante: Nessun link di menu punta a una bozza o a un indirizzo esterno non voluto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
