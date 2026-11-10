# Piano di validazione — Cambio di hosting o di dominio

## Modello di dati
Backup, nuovo hosting, DNS, reindirizzamenti di dominio.

## Implementazione attesa
Eseguire il backup, ripristinare presso il nuovo provider di hosting, verificare, commutare il DNS, reindirizzare il vecchio dominio pagina per pagina.

## Test da prevedere
1. Nominale: Provare il trasferimento su un dominio di test.
2. Controllo di rifiuto: Nessun vecchio indirizzo risponde con un 404 dopo la commutazione.
3. Invariante: I segreti del sito non viaggiano mai via e-mail o messaggistica.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
