# Piano di validazione — Mappe e indicazioni per raggiungere la sede

## Modello di dati
Indirizzo, coordinate, immagine della mappa, link al percorso.

## Implementazione attesa
Preferire un'immagine di mappa statica con link al percorso; una mappa interattiva di terze parti dipende dalla politica dei contenuti nativa.

## Test da prevedere
1. Nominale: Verificare immagine, testo alternativo e link al percorso su mobile.
2. Controllo di rifiuto: Nessuna richiesta verso un servizio di mappe al caricamento della pagina.
3. Invariante: Nessuna mappa di terze parti caricata prima di un'azione del visitatore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
