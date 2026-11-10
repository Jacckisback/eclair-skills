# Piano di validazione — Resi e rimborsi

## Modello di dati
Richiesta di reso, motivo, stato, rimborso.

## Implementazione attesa
Pubblicare la politica di reso nativa sulle schede, gestire le richieste tramite il modulo di contatto, rimborsare presso il fornitore; progettare il monitoraggio strutturato.

## Test da prevedere
1. Nominale: Seguire una richiesta di reso dalla ricezione al rimborso.
2. Controllo di rifiuto: Una richiesta fuori termine riceve una risposta motivata, non un rimborso automatico.
3. Invariante: Un rimborso è avviato soltanto da una persona autorizzata, presso il fornitore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
