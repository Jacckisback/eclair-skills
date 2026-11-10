# Piano di validazione — Pulsanti di condivisione

## Modello di dati
Social network, indirizzo di condivisione, etichetta.

## Implementazione attesa
Usare semplici link di condivisione e l'API di condivisione del browser come miglioramento progressivo.

## Test da prevedere
1. Nominale: Condividere una pagina da mobile e da computer.
2. Controllo di rifiuto: Nessuna richiesta verso terze parti prima del clic.
3. Invariante: Nessun pulsante carica script o tracker di terze parti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
