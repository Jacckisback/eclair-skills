# Piano di validazione — Categorie

## Modello di dati
Categoria, indirizzo, descrizione, contenuti associati.

## Implementazione attesa
Definire poche categorie stabili, redigerne la descrizione, associare ogni contenuto a una categoria principale.

## Test da prevedere
1. Nominale: Creare le categorie, associare i contenuti e verificare le pagine di categoria e la loro paginazione.
2. Controllo di rifiuto: Una categoria senza contenuti pubblicati non viene proposta nella navigazione.
3. Invariante: Non creare categorie vuote o duplicate che diluiscono il sito.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
