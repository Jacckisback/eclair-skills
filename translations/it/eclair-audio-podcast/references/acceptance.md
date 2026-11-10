# Piano di validazione — Audio e podcast

## Modello di dati
Episodio, file audio, durata, note, feed.

## Implementazione attesa
Creare una pagina per episodio con player HTML nativo, generare il feed del podcast in GET e ospitare i file pesanti fuori dal sito se necessario.

## Test da prevedere
1. Nominale: Validare il feed con un validatore di podcast e riprodurre un episodio su mobile.
2. Controllo di rifiuto: Un episodio in bozza è assente dal feed.
3. Invariante: Il feed fa riferimento soltanto a episodi pubblicati e a file pubblici.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
