# Piano di validazione — Misurazione dell'audience rispettosa

## Modello di dati
Pagina vista, sorgente, periodo, aggregati.

## Implementazione attesa
Preferire i log del server o uno strumento senza cookie self-hosted ; uno script di terze parti dipende dalla politica dei contenuti nativa.

## Test da prevedere
1. Nominale: Confrontare le pagine viste misurate con un percorso di test.
2. Controllo di rifiuto: Nessun cookie viene depositato dalla misurazione.
3. Invariante: Non viene conservato alcun indirizzo IP completo né identificatore del visitatore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
