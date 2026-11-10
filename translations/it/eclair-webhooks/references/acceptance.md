# Piano di validazione — Webhook in entrata e in uscita

## Modello di dati
Origine, segreto, evento, firma, data e ora, ID univoco, tentativo, risultato.

## Implementazione attesa
Specificare il contratto, verificare la firma sui byte grezzi, protezione anti-replay e coda persistente; documentare retries/dlq ed endpoint POST privato.

## Test da prevedere
1. Nominale: Testare doppio invio, ritardo, ordine invertito e segreto cambiato.
2. Controllo di rifiuto: Due tentativi dello stesso webhook attivano una sola mutazione applicativa.
3. Invariante: Non pubblicare mai un webhook con segreto nell'URL né elaborare un evento finanziario non firmato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
