# Piano di validazione — Campagne e-mail

## Modello di dati
Lista, segmento, campagna, invio, disiscrizione.

## Implementazione attesa
Affidare l'invio a un servizio specializzato, preparare i contenuti a partire dal sito, definire segmenti, frequenza e disiscrizione.

## Test da prevedere
1. Nominale: Inviare una campagna di test a una lista interna.
2. Controllo di rifiuto: Un indirizzo disiscritto non riceve più nulla.
3. Invariante: Ogni e-mail contiene un link di disiscrizione funzionante ; nessuna lista acquistata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
