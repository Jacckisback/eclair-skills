# Piano di validazione — Connettori API

## Modello di dati
OAuth/token, scope, quote, errori, paginazione, versione e log.

## Implementazione attesa
Definire lo schema dell'API, isolare i segreti, convalidare gli schemi in ingresso, prevedere timeout/circuit breaker e versionamento.

## Test da prevedere
1. Nominale: Testare timeout, 429, 500, risposta malformata e revoca.
2. Controllo di rifiuto: Un 500 del fornitore non danneggia i dati locali né la resa pubblica.
3. Invariante: Non consentire SSRF o URL dinamici arbitrari; non registrare mai un token nei log.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
