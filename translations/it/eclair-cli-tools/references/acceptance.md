# Piano di validazione — Strumenti da riga di comando

## Modello di dati
Comando, input, output, codice di uscita.

## Implementazione attesa
Su un checkout del core, avviare validatore, suite di test e misura dei budget; integrare questi comandi nella CI del progetto.

## Test da prevedere
1. Nominale: Convalidare un pacchetto e leggere il report JSON.
2. Controllo di rifiuto: Un pacchetto non valido fa fallire il comando e la CI.
3. Invariante: Nessun comando viene eseguito in produzione senza backup.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
