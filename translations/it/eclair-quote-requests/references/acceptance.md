# Piano di validazione — Richieste di preventivo

## Modello di dati
Richiesta, prestazione, budget, tempistiche, recapiti.

## Implementazione attesa
Iniziare con il modulo di contatto nativo e con domande guidate nella pagina ; progettare il modulo strutturato per un secondo momento.

## Test da prevedere
1. Nominale: Inviare una richiesta tipo e verificarne la ricezione completa.
2. Controllo di rifiuto: Una richiesta senza recapiti validi viene rifiutata con un messaggio chiaro.
3. Invariante: Vengono richiesti soltanto i dati utili al preventivo.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
