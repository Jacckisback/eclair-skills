# Piano di validazione — Accessibilità WCAG

## Modello di dati
Struttura dei titoli, navigazione da tastiera, focus, moduli, media, contrasti.

## Implementazione attesa
Eseguire un audit da tastiera e con screen reader, verificare axe-core, contrasti, messaggi di errore e movimento ridotto.

## Test da prevedere
1. Nominale: Testare percorsi senza mouse, errori dei moduli e zoom al 200%.
2. Controllo di rifiuto: Un modulo resta comprensibile senza colore e da tastiera.
3. Invariante: Non rimuovere il focus visibile né rendere una funzionalità dipendente unicamente dal colore o da un gesto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
