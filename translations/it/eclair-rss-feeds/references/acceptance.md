# Piano di validazione — Feed RSS

## Modello di dati
Feed, elementi, data, contenuto completo o estratto.

## Implementazione attesa
Controllare il feed prodotto dal core, dichiararlo nelle pagine, proporlo agli abbonati e agli aggregatori.

## Test da prevedere
1. Nominale: Validare il feed con un lettore e un validatore.
2. Controllo di rifiuto: Un contenuto non più pubblicato scompare dal feed alla rigenerazione.
3. Invariante: Il feed contiene soltanto contenuti pubblicati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
