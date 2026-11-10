# Piano di validazione — Piattaforme di automazione

## Modello di dati
Scenario, attivatore, dati trasmessi.

## Implementazione attesa
Esporre in lettura ciò che la piattaforma può interrogare (feed, JSON pubblico); progettare la ricezione di eventi per un secondo momento.

## Test da prevedere
1. Nominale: Far leggere un feed pubblico dalla piattaforma e attivare uno scenario.
2. Controllo di rifiuto: Una chiamata in entrata non autenticata non modifica nulla sul sito.
3. Invariante: Nessun dato personale viene esposto in un endpoint pubblico per agevolare un'automazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
