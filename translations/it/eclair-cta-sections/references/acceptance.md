# Piano di validazione — Inviti all'azione

## Modello di dati
Titolo, testo, pulsante, destinazione.

## Implementazione attesa
Definire un'azione principale per pagina, ripeterla nei punti giusti, verificare contrasto ed etichetta esplicita.

## Test da prevedere
1. Nominale: Seguire ogni pulsante fino alla sua destinazione su mobile.
2. Controllo di rifiuto: Un pulsante senza destinazione valida non viene pubblicato.
3. Invariante: Nessun link ingannevole né reindirizzamento aperto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
