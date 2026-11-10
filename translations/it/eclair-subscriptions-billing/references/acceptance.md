# Piano di validazione — Abbonamenti a pagamento

## Modello di dati
Offerta, periodo, abbonato, scadenza, stato.

## Implementazione attesa
Lasciare che il fornitore gestisca addebiti e area clienti ; progettare la sincronizzazione dei permessi tramite eventi firmati.

## Test da prevedere
1. Nominale: Simulare sottoscrizione, rinnovo, mancato pagamento e disdetta.
2. Controllo di rifiuto: Un pagamento non riuscito non prolunga alcun accesso.
3. Invariante: Un permesso di accesso viene aperto soltanto a fronte di un evento di pagamento autenticato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
