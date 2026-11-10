# Piano di validazione — Assistenza e ticket

## Modello di dati
Ticket, richiedente, stato, scambi, priorità.

## Implementazione attesa
Iniziare con modulo di contatto e casella di posta in arrivo; progettare stati, tempi di risposta e area di monitoraggio per un secondo momento.

## Test da prevedere
1. Nominale: Seguire una richiesta dall'apertura alla chiusura.
2. Controllo di rifiuto: Un ticket non può essere letto indovinandone il numero.
3. Invariante: Un richiedente vede soltanto i propri ticket.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
