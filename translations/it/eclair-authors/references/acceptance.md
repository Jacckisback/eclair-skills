# Piano di validazione — Autori e firme

## Modello di dati
Autore, biografia, ruolo, link, contenuti firmati.

## Implementazione attesa
Completare i profili reali, collegare ogni articolo al suo autore, verificare la pagina autore e i dati strutturati prodotti dal core.

## Test da prevedere
1. Nominale: Compilare un profilo e verificare firma, pagina autore e markup.
2. Controllo di rifiuto: Un account disattivato o senza contenuti pubblicati non espone alcuna pagina autore.
3. Invariante: Non inventare mai un autore, un titolo di studio o un'esperienza.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
