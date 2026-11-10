# Piano di validazione — Performance UX

## Modello di dati
LCP, CLS, INP, peso degli asset, CSS, JS, cache e font.

## Implementazione attesa
Misurare prima/dopo tramite tools/measure.php --check, Chrome Lighthouse e rete lenta, ottimizzare immagini e script.

## Test da prevedere
1. Nominale: Testare il sito pubblico senza estensione, con estensione e su mobile.
2. Controllo di rifiuto: Un miglioramento dichiarato è accompagnato da misure riproducibili prima/dopo.
3. Invariante: Non degradare il percorso di cache PHP né disattivare la CSP per comodità.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
