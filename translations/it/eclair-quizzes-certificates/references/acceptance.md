# Piano di validazione — Quiz e attestati

## Modello di dati
Domanda, scelte, correzione, tentativo, punteggio, tempo limite, attestato e verifica.

## Implementazione attesa
Versionare la banca di domande; assegnare il punteggio lato server; definire tentativi e tempi; generare un attestato firmato/verificabile senza PII pubbliche.

## Test da prevedere
1. Nominale: Testare imbroglio, fine della sessione, convalida del certificato.
2. Controllo di rifiuto: Inviare due volte un tentativo non deve generare due certificati.
3. Invariante: Non inviare mai la soluzione o la risposta esatta nell'HTML di una prova attiva.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
