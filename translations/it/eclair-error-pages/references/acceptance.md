# Piano di validazione — Pagine di errore

## Modello di dati
Pagina di errore, link utili, registro degli indirizzi non trovati.

## Implementazione attesa
Comporre una pagina 404 utile nel tema del sito, proporre home page e pagine chiave, gestire i 404 frequenti tramite reindirizzamento.

## Test da prevedere
1. Nominale: Richiedere un indirizzo inesistente e verificare stato 404 e contenuto.
2. Controllo di rifiuto: Una pagina non trovata non risponde mai con uno stato 200.
3. Invariante: La pagina di errore non mostra alcuna traccia tecnica.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
