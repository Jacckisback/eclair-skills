# Piano di validazione — Carrello e percorso d'ordine

## Modello di dati
Carrello temporaneo, sessione membro o ospite, righe, promozioni, spese, imposte, stato dell'ordine.

## Implementazione attesa
Separare visualizzazione e cambio di stato; riconvalidare ogni riga sul server; calcolare gli importi in unità monetarie intere; riservare lo stock in modo transazionale al momento giusto.

## Test da prevedere
1. Nominale: Testare modifica simultanea del carrello, scadenza e cambio di prezzo.
2. Controllo di rifiuto: Un invio doppio o concorrente non crea due ordini pagabili per la stessa chiave.
3. Invariante: Nessuna operazione di scrittura pubblica prima di route POST qualificata, CSRF, quote e permessi verificati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
