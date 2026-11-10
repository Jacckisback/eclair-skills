# Piano di validazione — Richieste relative ai dati

## Modello di dati
Richiesta, persona, dati interessati, termine, risposta.

## Implementazione attesa
Mappare dove si trovano i dati (messaggi, account, log, backup), scrivere la procedura di accesso e di cancellazione, tenere un registro.

## Test da prevedere
1. Nominale: Seguire una richiesta di accesso e poi di cancellazione su un set di dati di test.
2. Controllo di rifiuto: Una richiesta senza verifica dell'identità non porta ad alcuna divulgazione.
3. Invariante: L'identità del richiedente viene verificata prima di qualsiasi comunicazione di dati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
