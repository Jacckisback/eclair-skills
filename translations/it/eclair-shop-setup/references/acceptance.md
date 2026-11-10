# Piano di validazione — Apertura del negozio leggero

## Modello di dati
Prodotto, prezzo, categoria, note legali, condizioni di vendita.

## Implementazione attesa
Pubblicare note legali e condizioni di vendita, aprire il negozio, creare le prime schede, verificare catalogo e dati strutturati.

## Test da prevedere
1. Nominale: Aprire il negozio su una copia e percorrere catalogo e scheda.
2. Controllo di rifiuto: Il negozio non si apre senza pagine legali pubblicate.
3. Invariante: Nessun prezzo, termine o condizione di vendita inventati dall'agente.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
