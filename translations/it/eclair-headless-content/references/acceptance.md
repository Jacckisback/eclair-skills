# Piano di validazione — Contenuto per applicazioni e IA

## Modello di dati
Versione Markdown, llms.txt, feed, sitemap.

## Implementazione attesa
Basarsi sugli output nativi leggibili dalle macchine, documentarne formato e freschezza per l'applicazione client.

## Test da prevedere
1. Nominale: Leggere una pagina in HTML e in Markdown e confrontare.
2. Controllo di rifiuto: Una bozza non ha una versione Markdown accessibile.
3. Invariante: Nessun contenuto privato viene esposto da questi output.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
