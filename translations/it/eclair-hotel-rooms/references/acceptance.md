# Piano di validazione — Alloggi e camere

## Modello di dati
Camera, capienza, dotazioni, tariffe indicative, link di prenotazione.

## Implementazione attesa
Presentare ogni alloggio in una scheda, rimandare al motore di prenotazione esistente o alla richiesta tramite modulo.

## Test da prevedere
1. Nominale: Scorrere le schede e il link di prenotazione su mobile.
2. Controllo di rifiuto: Una camera ritirata non viene più proposta.
3. Invariante: Nessuna disponibilità né tariffa mostrata come garantita se non proviene dal sistema di prenotazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
