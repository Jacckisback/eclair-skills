# Piano di validazione — Simulatori e calcolatori

## Modello di dati
Parametri, formula, risultato.

## Implementazione attesa
Calcolare nel browser con una formula validata dal cliente, mostrare ipotesi e limiti, proporre poi il contatto.

## Test da prevedere
1. Nominale: Confrontare i risultati con un insieme di casi calcolati a mano.
2. Controllo di rifiuto: Un valore assurdo o negativo mostra un messaggio, non un risultato errato.
3. Invariante: Il risultato è indicativo e presentato come tale ; nessun dato inserito viene inviato al server.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
