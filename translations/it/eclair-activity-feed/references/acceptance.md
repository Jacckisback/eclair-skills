# Piano di validazione — Flusso di attività

## Modello di dati
Evento, autore, visibilità, data.

## Implementazione attesa
Definire quali eventi vengono pubblicati, per chi, e come un membro li nasconde o li elimina.

## Test da prevedere
1. Nominale: Simulare pubblicazioni con visibilità diverse.
2. Controllo di rifiuto: Un contenuto eliminato scompare anche dal flusso.
3. Invariante: Nessuna attività privata viene rivelata in un flusso pubblico.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
