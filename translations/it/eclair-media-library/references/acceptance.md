# Piano di validazione — Libreria multimediale

## Modello di dati
File, testo alternativo, dimensioni, utilizzi.

## Implementazione attesa
Importare i media, compilare i testi alternativi, individuare i file inutilizzati e i duplicati.

## Test da prevedere
1. Nominale: Caricare più formati e verificare conversione, dimensioni e testi alternativi.
2. Controllo di rifiuto: Un file in formato vietato o malevolo viene rifiutato al caricamento.
3. Invariante: Vengono caricati soltanto i formati accettati dal core ; nessun file eseguibile.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
