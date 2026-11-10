# Piano di validazione — Gruppi

## Modello di dati
Gruppo, visibilità, membri, ruoli.

## Implementazione attesa
Definire creazione, adesione, ruoli e visibilità; applicare i permessi a ogni lettura.

## Test da prevedere
1. Nominale: Simulare creazione, richiesta di adesione ed esclusione.
2. Controllo di rifiuto: Un non membro non legge alcun contenuto di un gruppo privato.
3. Invariante: Il contenuto di un gruppo privato non compare né nella ricerca né nella cache pubblica.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
