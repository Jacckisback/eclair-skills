# Piano di validazione — Abbonamenti e adesioni

## Modello di dati
Piano, adesione, rinnovo, periodo, disdetta, pagamento, diritto.

## Implementazione attesa
Calcolare i diritti a partire dallo stato verificato, prevedere cambi di piano e periodi di tolleranza, gestire gli eventi di fatturazione in modo idempotente.

## Test da prevedere
1. Nominale: Testare addebito fallito, calcolo pro rata, rimborso e disdetta.
2. Controllo di rifiuto: Due eventi identici non prolungano l'abbonamento due volte.
3. Invariante: Una ricevuta proveniente dal browser non basta mai per rinnovare un accesso a pagamento.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
