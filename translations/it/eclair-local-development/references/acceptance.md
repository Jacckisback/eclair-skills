# Piano di validazione — Sviluppo locale

## Modello di dati
Versione di PHP, server web, copia del sito, dati di test.

## Implementazione attesa
Installare la stessa versione di PHP e le stesse regole del server, ripristinare un backup anonimizzato, avviare i test.

## Test da prevedere
1. Nominale: Avviare il sito locale e far passare la suite di test.
2. Controllo di rifiuto: Una copia locale non invia alcuna e-mail reale.
3. Invariante: I dati reali dei clienti non vengono copiati in locale senza anonimizzazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
