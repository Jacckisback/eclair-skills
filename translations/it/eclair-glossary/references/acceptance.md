# Piano di validazione — Glossario

## Modello di dati
Termine, definizione, termini correlati.

## Implementazione attesa
Redigere una definizione chiara per ogni termine, ordinare alfabeticamente, collegare i termini ai contenuti che li usano.

## Test da prevedere
1. Nominale: Navigare per lettera e seguire i link tra i termini.
2. Controllo di rifiuto: Un termine senza definizione convalidata non viene pubblicato.
3. Invariante: Nessuna definizione copiata da una fonte protetta.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
