# Piano di validazione — Pubblicità

## Modello di dati
Posizione, consenso, file ads.txt.

## Implementazione attesa
Usare la pagina Pubblicità nativa, limitare le posizioni, verificare consenso, etichetta e impatto sulla velocità.

## Test da prevedere
1. Nominale: Misurare la pagina con e senza pubblicità e verificare il consenso.
2. Controllo di rifiuto: Le pagine diverse dagli articoli non mostrano pubblicità.
3. Invariante: Nessuna pubblicità caricata prima del consenso richiesto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
