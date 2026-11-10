# Piano di validazione — Conti alla rovescia

## Modello di dati
Data di destinazione, fuso orario, messaggio finale.

## Implementazione attesa
Scrivere la data nell'HTML, animare come miglioramento progressivo, prevedere lo stato dopo la scadenza e l'invalidazione della cache.

## Test da prevedere
1. Nominale: Testare prima, durante e dopo la scadenza e in due fusi orari.
2. Controllo di rifiuto: Dopo la scadenza, la pagina in cache non mostra più un'offerta scaduta.
3. Invariante: Nessuna falsa urgenza: la data corrisponde a un evento reale.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
