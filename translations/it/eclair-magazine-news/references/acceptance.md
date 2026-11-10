# Piano di validazione — Magazine e notizie

## Modello di dati
Articolo, sezione, autore, prima pagina, data.

## Implementazione attesa
Strutturare sezioni e prima pagina, curare autori e date, usare le funzionalità native per i media (immagini grandi, pianificazione, feed).

## Test da prevedere
1. Nominale: Pubblicare una prima pagina di test e verificare sezioni, feed e sitemap.
2. Controllo di rifiuto: Un articolo corretto mostra la propria data di aggiornamento.
3. Invariante: Nessuna informazione priva di fonte presentata come un fatto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
