# Piano di validazione — Design system

## Modello di dati
Token, griglia, spaziature, colori, tipografia, componenti e stati.

## Implementazione attesa
Dichiarare la scala dei token, riutilizzare i componenti, documentare stati e varianti; compatibilità con il tema Éclair.

## Test da prevedere
1. Nominale: Testare contrasto, coerenza e cambio di tema.
2. Controllo di rifiuto: Cambiare il colore principale non rende illeggibili i link né i messaggi di errore.
3. Invariante: Non introdurre fogli CSS pesanti o librerie JS senza prova della necessità.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
