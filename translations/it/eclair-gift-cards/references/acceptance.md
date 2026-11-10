# Piano di validazione — Carte regalo

## Modello di dati
Carta, codice, saldo, validità.

## Implementazione attesa
Generare codici imprevedibili, tenere traccia del saldo lato server, gestire la scadenza secondo la legge applicabile.

## Test da prevedere
1. Nominale: Simulare acquisto, utilizzo parziale e saldo residuo.
2. Controllo di rifiuto: Un codice esaurito o scaduto viene rifiutato.
3. Invariante: Un codice non è mai indovinabile né riutilizzabile oltre il proprio saldo.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
