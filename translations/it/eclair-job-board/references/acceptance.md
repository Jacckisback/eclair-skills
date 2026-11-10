# Piano di validazione — Offerte di lavoro

## Modello di dati
Offerta, azienda, stato, scadenza, candidatura e allegati.

## Implementazione attesa
Costruire filtri pubblici, scadenza automatica, moduli sicuri e ciclo di conservazione delle candidature.

## Test da prevedere
1. Nominale: Testare annuncio scaduto, spam ed esportazione del candidato.
2. Controllo di rifiuto: Un selezionatore non può leggere una candidatura destinata a un'altra azienda.
3. Invariante: CV e allegati non vengono mai collocati in una directory web accessibile.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
