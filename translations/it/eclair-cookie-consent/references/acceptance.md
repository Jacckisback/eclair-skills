# Piano di validazione — Cookie e consenso

## Modello di dati
Tracker, finalità, consenso, prova.

## Implementazione attesa
Inventariare i tracker reali; senza tracker, niente banner; altrimenti consenso preventivo, rifiuto semplice quanto l'accettazione e pagina informativa.

## Test da prevedere
1. Nominale: Ispezionare cookie e richieste prima e dopo la scelta.
2. Controllo di rifiuto: Dopo un rifiuto, nessun tracker di terze parti viene caricato.
3. Invariante: Nessun tracker soggetto a consenso viene installato prima dell'accettazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
