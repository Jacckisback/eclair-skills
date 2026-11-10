# Piano di validazione — Notifiche della community

## Modello di dati
Sottoscrizione, menzione, notifica, canale, preferenza, stato.

## Implementazione attesa
Emettere gli eventi dopo una scrittura convalidata, filtrare in base ai permessi al momento della lettura e dell'invio, applicare la disiscrizione.

## Test da prevedere
1. Nominale: Testare notifiche ripetute, disiscrizione e revoca del permesso.
2. Controllo di rifiuto: Dopo la revoca dell'accesso, nessuna nuova notifica contiene un estratto privato.
3. Invariante: Non rivelare mai il contenuto di categorie private in email, push o digest.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
