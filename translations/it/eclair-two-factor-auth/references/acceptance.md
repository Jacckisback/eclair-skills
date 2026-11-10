# Piano di validazione — Autenticazione a due fattori

## Modello di dati
Account, segreto TOTP, codici di emergenza.

## Implementazione attesa
Far attivare l'autenticazione a due fattori da ogni persona, riporre i codici di emergenza, prevedere la perdita del dispositivo.

## Test da prevedere
1. Nominale: Attivare, disconnettersi, riconnettersi con il secondo fattore.
2. Controllo di rifiuto: Una password corretta senza secondo fattore non dà accesso.
3. Invariante: I segreti e i codici di emergenza non vengono mai copiati in una chat, in un'e-mail o in un repository.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
