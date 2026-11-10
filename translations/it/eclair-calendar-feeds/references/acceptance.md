# Piano di validazione — Feed di calendario

## Modello di dati
Evento, data, fuso orario, luogo, feed iCalendar.

## Implementazione attesa
Generare un feed iCalendar pubblico in GET a partire dagli eventi pubblicati, con fusi orari espliciti.

## Test da prevedere
1. Nominale: Abbonarsi al feed da due applicazioni di calendario.
2. Controllo di rifiuto: Un evento annullato è contrassegnato come annullato nel feed.
3. Invariante: Il feed contiene soltanto eventi pubblici, senza partecipanti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
