# Piano di validazione — Audit SEO tecnico

## Modello di dati
URL, canonical, sitemap, reindirizzamenti, titoli, stati HTTP, dati strutturati.

## Implementazione attesa
Eseguire il crawling delle pagine autorizzate, rilevare le divergenze, dare priorità alle cause strutturali, verificare copertura e piano di correzione.

## Test da prevedere
1. Nominale: Testare slash, accenti, paginazioni, 404, sitemap e robots.
2. Controllo di rifiuto: Nessun URL critico è orfano o reindirizzato a catena dopo l'aggiornamento.
3. Invariante: Non promettere posizionamenti; non modificare gli URL esistenti senza un piano dei redirect.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
