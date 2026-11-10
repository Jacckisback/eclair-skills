# Piano di validazione — Cache delle pagine

## Modello di dati
Pagina in cache, invalidazione, varianti vietate.

## Implementazione attesa
Misurare la risposta in cache, individuare ciò che impedisce la messa in cache di una route di estensione, verificare l'invalidazione alla modifica.

## Test da prevedere
1. Nominale: Misurare il tempo di risposta prima e dopo una modifica.
2. Controllo di rifiuto: Una route di estensione dichiarata non memorizzabile in cache non viene mai servita dalla cache.
3. Invariante: Nessuna pagina contenente dati di sessione o personali entra nella cache condivisa.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
