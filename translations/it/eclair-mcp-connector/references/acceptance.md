# Piano di validazione — Connettore MCP

## Modello di dati
Client autorizzato, token, strumenti disponibili, bozze create.

## Implementazione attesa
Far attivare il connettore dal proprietario, autorizzare il client, lavorare con bozze e proposte, saper interrompere l'accesso.

## Test da prevedere
1. Nominale: Creare una bozza tramite il connettore e poi revocare l'accesso.
2. Controllo di rifiuto: Dopo la revoca, ogni richiesta del client viene rifiutata.
3. Invariante: Il connettore non pubblica né elimina; l'accesso è revocabile in qualsiasi momento.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
