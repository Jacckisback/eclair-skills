# Piano di validazione — Barre di annuncio

## Modello di dati
Messaggio, link, date di inizio e di fine.

## Implementazione attesa
Rendere la barra lato server con date di validità, senza spostamento del layout, rimossa automaticamente alla scadenza.

## Test da prevedere
1. Nominale: Mostrare, chiudere e lasciar scadere una barra.
2. Controllo di rifiuto: Dopo la data di fine, la barra non compare più su alcuna pagina.
3. Invariante: Nessun annuncio scaduto resta servito dalla cache.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
