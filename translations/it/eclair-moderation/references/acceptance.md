# Piano di validazione — Moderazione e segnalazioni

## Modello di dati
Segnalazione, motivo, elemento interessato, decisione, moderatore, audit.

## Implementazione attesa
Prevedere coda di gestione, segnalazioni abusive, soglie/quote, rollback e motivazioni; tracciare le decisioni e limitare i poteri per ruolo.

## Test da prevedere
1. Nominale: Testare moderatore senza permesso globale, utente sospeso e ricorso.
2. Controllo di rifiuto: Il moderatore di una categoria non può vedere le segnalazioni private di un'altra.
3. Invariante: Nessuna eliminazione definitiva automatica su segnalazione senza controllo e prove.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
