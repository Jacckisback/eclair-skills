# Piano di validazione — Contenuti multilingue

## Modello di dati
Contenuto, lingua, versione collegata, indirizzo per lingua.

## Implementazione attesa
Verificare nelle capacità le lingue supportate dal sito, organizzare una struttura ad albero per lingua, collegare le versioni e controllare hreflang.

## Test da prevedere
1. Nominale: Creare una pagina in due lingue e verificare link incrociati e hreflang.
2. Controllo di rifiuto: Una lingua senza traduzione non rimanda a una pagina vuota.
3. Invariante: Nessuna traduzione automatica pubblicata senza revisione umana.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
