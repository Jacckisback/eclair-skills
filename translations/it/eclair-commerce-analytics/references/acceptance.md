# Piano di validazione — Misurazione delle vendite

## Modello di dati
Funnel, ordini confermati, rimborsi, tasso di conversione, ricavi netti, consensi.

## Implementazione attesa
Definire eventi e metriche senza riutilizzare dati sensibili; riconciliare totali degli ordini, note di credito e pagamenti; prevedere una sintesi aggregata.

## Test da prevedere
1. Nominale: Testare ricavi dopo un rimborso e interruzione del conteggio.
2. Controllo di rifiuto: L'aggregazione non deve né contare due volte lo stesso pagamento né divulgare un ordine identificabile.
3. Invariante: I dati analitici personali richiedono una base giuridica e non devono trapelare attraverso la cache.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
