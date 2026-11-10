# Piano di validazione — Iscrizione alla newsletter

## Modello di dati
Indirizzo e-mail, consenso, data, origine.

## Implementazione attesa
Usare una pagina di iscrizione ospitata dal servizio di e-mail marketing o un link, finché il sito non può ricevere iscrizioni direttamente ; doppia conferma.

## Test da prevedere
1. Nominale: Iscriversi, confermare, disiscriversi.
2. Controllo di rifiuto: Un'iscrizione non confermata non riceve alcun invio.
3. Invariante: Nessun indirizzo viene aggiunto a una lista senza consenso esplicito e prova.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
