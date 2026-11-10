# Piano di validazione — Diagnostica e log

## Modello di dati
Sintomo, log del server, log del sito, ipotesi, correzione.

## Implementazione attesa
Riprodurre, leggere i log del server e del sito, isolare la funzionalità responsabile disattivandola, correggere e poi verificare.

## Test da prevedere
1. Nominale: Provocare un errore in un'estensione di test e localizzarlo.
2. Controllo di rifiuto: Nessuna traccia tecnica compare in una pagina pubblica.
3. Invariante: La visualizzazione degli errori non viene mai attivata sul sito pubblico.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
