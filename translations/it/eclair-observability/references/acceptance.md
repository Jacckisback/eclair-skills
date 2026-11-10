# Piano di validazione — Osservabilità e avvisi

## Modello di dati
Log strutturati, errori, correlazioni, metriche, tracce, conservazione.

## Implementazione attesa
Definire avvisi utili, anonimizzare i dati, sorvegliare task e cache, distinguere incidente del sito e del modulo, fornire un runbook.

## Test da prevedere
1. Nominale: Testare aumento degli errori 5xx, ritardo dei task e disco pieno.
2. Controllo di rifiuto: Un modulo disattivato non continua a inviare dati né a eseguire task.
3. Invariante: Nessuna password, token, pagamento o PII grezza nei log; nessuna telemetria nascosta.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
