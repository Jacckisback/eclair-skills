# Piano di validazione — Prodotti digitali

## Modello di dati
Prodotto digitale, acquisto, link di consegna temporaneo.

## Implementazione attesa
Far consegnare il file dal fornitore o tramite link firmato a durata limitata; non collocare mai il file a un indirizzo pubblico.

## Test da prevedere
1. Nominale: Simulare acquisto, consegna e scadenza del link.
2. Controllo di rifiuto: Un link scaduto o condiviso non dà più accesso al file.
3. Invariante: Nessun file a pagamento è accessibile senza acquisto verificato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
