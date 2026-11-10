# Piano di validazione — Reindirizzamenti

## Modello di dati
Vecchio indirizzo, nuovo indirizzo, tipo, data.

## Implementazione attesa
Importare i vecchi indirizzi, creare un reindirizzamento diretto per indirizzo, eliminare catene e loop.

## Test da prevedere
1. Nominale: Testare un lotto di vecchi indirizzi e rilevare stato e destinazione.
2. Controllo di rifiuto: Nessuna catena di più di un salto né loop.
3. Invariante: Nessun reindirizzamento aperto verso un dominio non voluto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
