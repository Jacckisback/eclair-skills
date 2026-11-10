# Piano di validazione — Link di pagamento

## Modello di dati
Prodotto o variante, link di pagamento, fornitore.

## Implementazione attesa
Creare il link presso il fornitore, incollarlo nella scheda o nella variante, testare in modalità test, verificare ricevuta e rimborso lato fornitore.

## Test da prevedere
1. Nominale: Acquistare in modalità test e verificare importo e ricevuta.
2. Controllo di rifiuto: Un link verso un dominio non riconosciuto viene rifiutato.
3. Invariante: Nessun dato bancario sul sito ; un link porta soltanto al dominio del fornitore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
