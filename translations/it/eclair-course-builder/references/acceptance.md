# Piano di validazione — Creazione di percorsi

## Modello di dati
Corso, modulo, lezione, ordine, bozza, versione pubblicata e autore.

## Implementazione attesa
Stabilire uno schema gerarchico; visualizzare l'anteprima prima della pubblicazione; preservare gli identificativi durante il riordinamento; documentare l'archiviazione.

## Test da prevedere
1. Nominale: Testare scambio di lezioni, ritiro dalla pubblicazione e modifica concorrente.
2. Controllo di rifiuto: Cambiare l'ordine non azzera i progressi degli studenti.
3. Invariante: Le bozze del formatore non devono essere indicizzate né esposte pubblicamente.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
