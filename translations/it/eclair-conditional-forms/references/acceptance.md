# Piano di validazione — Moduli condizionali

## Modello di dati
Campo, condizione, ramo, validazione.

## Implementazione attesa
Descrivere le regole sotto forma di dati, applicarle lato server e lato browser, testare ogni ramo.

## Test da prevedere
1. Nominale: Percorrere ogni ramo fino all'invio.
2. Controllo di rifiuto: Un campo obbligatorio di un ramo attivo non può essere aggirato.
3. Invariante: La validazione lato server non si fida mai dei campi nascosti lato browser.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
