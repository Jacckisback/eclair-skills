# Piano di validazione — Creazione di temi

## Modello di dati
theme.json, stili, asset, template dichiarati, licenza e provenienza.

## Implementazione attesa
Partire dal tema di esempio ufficiale, impiegare variabili e template supportati, testare la preview e poi lo ZIP, verificare la compatibilità di versione.

## Test da prevedere
1. Nominale: Testare validatore del tema, attivazione, anteprima e ripristino.
2. Controllo di rifiuto: Un template difettoso non rende il sito inaccessibile grazie al ripiego previsto.
3. Invariante: Non rifare mai SEO head e canonical né toccare i file del core.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
