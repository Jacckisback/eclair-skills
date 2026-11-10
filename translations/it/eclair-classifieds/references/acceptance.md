# Piano di validazione — Piccoli annunci

## Modello di dati
Annuncio, inserzionista, categoria, stato, segnalazione.

## Implementazione attesa
Definire inserimento, moderazione, durata, segnalazione e messa in contatto senza esporre i recapiti.

## Test da prevedere
1. Nominale: Simulare inserimento, moderazione, scadenza e segnalazione.
2. Controllo di rifiuto: Un annuncio rifiutato o scaduto non è più accessibile.
3. Invariante: Nessun annuncio pubblicato senza moderazione; recapiti mai mostrati in chiaro.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
