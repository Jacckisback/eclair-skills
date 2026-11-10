# Piano di validazione — Profili della community

## Modello di dati
Pseudonimo univoco, avatar, preferenze di visibilità, reputazione e ruoli.

## Implementazione attesa
Distinguere ID interno e pseudonimo; imporre limiti e moderazione dell'avatar; esporre unicamente i campi per cui c'è consenso; gestire cambi di nome e reindirizzamenti sicuri.

## Test da prevedere
1. Nominale: Testare collisione di pseudonimi ed eliminazione dell'account.
2. Controllo di rifiuto: Un visitatore non può dedurre un'email da un messaggio di errore o da un'API di profilo.
3. Invariante: Email, sessione, IP, indirizzo e informazioni di recupero restano privati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
