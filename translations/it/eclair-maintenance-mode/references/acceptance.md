# Piano di validazione — Modalità manutenzione

## Modello di dati
Stato di manutenzione, messaggio, durata prevista, accesso del team.

## Implementazione attesa
Servire una pagina statica con il corretto stato HTTP temporaneo a livello di server, mantenere l'accesso all'amministrazione, prevedere la rimessa online.

## Test da prevedere
1. Nominale: Attivare, verificare stato 503 e header di nuovo tentativo, disattivare.
2. Controllo di rifiuto: I bot non ricevono mai la pagina di manutenzione con uno stato 200.
3. Invariante: La pagina di manutenzione non rivela né versione né percorso del server.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
