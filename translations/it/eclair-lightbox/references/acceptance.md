# Piano di validazione — Visualizzatore di immagini

## Modello di dati
Immagine, versione ingrandita, didascalia.

## Implementazione attesa
Usare dialog nativo o link all'immagine, gestire focus, tasto Esc e ritorno, senza dipendenze.

## Test da prevedere
1. Nominale: Aprire, navigare e chiudere da tastiera.
2. Controllo di rifiuto: Senza JavaScript, il clic apre semplicemente l'immagine.
3. Invariante: Il focus viene intrappolato e poi restituito correttamente ; nessun contenuto esterno.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
