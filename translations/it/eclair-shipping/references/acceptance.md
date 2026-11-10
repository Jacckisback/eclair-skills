# Piano di validazione — Consegna e trasporto

## Modello di dati
Indirizzo validato, zona, corriere, collo, peso, servizio, spese, tracking.

## Implementazione attesa
Modellare zone e incompatibilità; calcolare il preventivo lato server; prevedere split shipments e consegna parziale; anonimizzare i dati di spedizione nei log.

## Test da prevedere
1. Nominale: Testare zona non servita, peso limite, due colli e stato smarrito.
2. Controllo di rifiuto: Un numero di tracciamento di un cliente non deve essere visibile da un altro account.
3. Invariante: Indirizzo e tracciamento sono privati; nessun dato personale in cache pubblica, log dettagliati o URL.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
