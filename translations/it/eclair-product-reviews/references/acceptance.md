# Piano di validazione — Recensioni dei prodotti

## Modello di dati
Recensione, voto, autore, acquisto verificato, stato.

## Implementazione attesa
Definire prova d'acquisto, moderazione, diritto di replica e visualizzazione aggregata; nel frattempo proporre testimonianze raccolte manualmente.

## Test da prevedere
1. Nominale: Simulare invio, moderazione e pubblicazione di una recensione.
2. Controllo di rifiuto: Una recensione senza acquisto verificato non è contrassegnata come verificata.
3. Invariante: Nessuna recensione pubblicata senza moderazione; nessun voto aggregato senza recensioni reali.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
