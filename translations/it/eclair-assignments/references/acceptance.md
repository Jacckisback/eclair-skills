# Piano di validazione — Compiti e correzioni

## Modello di dati
Compito, consegna, voto, commento, studente.

## Implementazione attesa
Definire consegna, scadenze, correzione e riscontro; isolare ogni elaborato rendendolo accessibile solo al suo autore e al correttore.

## Test da prevedere
1. Nominale: Simulare consegna, correzione e consultazione del voto.
2. Controllo di rifiuto: Uno studente non può accedere all'elaborato di un altro.
3. Invariante: Un elaborato è leggibile soltanto dal suo autore e dai correttori designati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
