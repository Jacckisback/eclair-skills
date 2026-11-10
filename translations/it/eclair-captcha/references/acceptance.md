# Piano di validazione — Captcha

## Modello di dati
Sfida, token, verifica lato server.

## Implementazione attesa
Preferire campo trappola e limiti nativi; un captcha di terze parti richiede un'apertura della politica dei contenuti che il core non delega alle estensioni.

## Test da prevedere
1. Nominale: Verificare che la protezione scelta blocchi un invio automatizzato.
2. Controllo di rifiuto: Nessuno script di captcha viene caricato sulle pagine senza modulo.
3. Invariante: Non indebolire mai la Content-Security-Policy del sito per caricare uno script di terze parti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
