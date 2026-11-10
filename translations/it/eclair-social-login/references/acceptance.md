# Piano di validazione — Accesso con account di terze parti

## Modello di dati
Provider di identità, account collegato, consenso.

## Implementazione attesa
Dipende anzitutto dagli account dei membri; progettare il flusso OAuth con state, PKCE e collegamento esplicito dell'account.

## Test da prevedere
1. Nominale: Simulare accesso, collegamento e scollegamento.
2. Controllo di rifiuto: Una risposta OAuth riprodotta o falsificata viene rifiutata.
3. Invariante: Nessun account viene unito sulla sola base di un indirizzo e-mail non verificato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
