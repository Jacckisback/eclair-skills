# Piano di validazione — Ordini e pagamenti

## Modello di dati
Ordine, tentativo di pagamento, identificativo del fornitore, prova del webhook, idempotency key, rimborso.

## Implementazione attesa
Dettagliare le transizioni autorizzate; archiviare la prova della notifica e la sua marca temporale; elaborare i webhook in modo durevole; prevedere reconciliation e rimborso parziale.

## Test da prevedere
1. Nominale: Testare webhook invertito, fuori ordine, riemesso e pagamento rifiutato.
2. Controllo di rifiuto: Un webhook senza firma valida non modifica né l'ordine né l'accesso LMS.
3. Invariante: Non archiviare mai dati grezzi di carte bancarie; checkout ospitato presso il fornitore e firma dei webhook verificata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
