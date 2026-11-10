# Piano di validazione — Sito per libera professione

## Modello di dati
Prestazione, professionista, onorari indicativi, richiesta di contatto.

## Implementazione attesa
Presentare ambiti di intervento e percorsi reali, rispettare le regole di comunicazione della professione, proporre contatto o appuntamento.

## Test da prevedere
1. Nominale: Far rileggere i contenuti dal professionista.
2. Controllo di rifiuto: Una specializzazione non riconosciuta non viene mostrata come titolo.
3. Invariante: Nessuna promessa di risultato né menzione vietata dalla deontologia della professione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
