# Piano di validazione — Sitemap XML

## Modello di dati
Voci della sitemap, date, immagini, lingue.

## Implementazione attesa
Controllare la sitemap prodotta dal core, dichiararla negli strumenti dei motori, monitorare gli errori di copertura.

## Test da prevedere
1. Nominale: Validare la sitemap e confrontarla con il numero di pagine pubblicate.
2. Controllo di rifiuto: Una pagina in bozza o reindirizzata non vi compare.
3. Invariante: La sitemap elenca soltanto pagine pubblicate e indicizzabili.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
