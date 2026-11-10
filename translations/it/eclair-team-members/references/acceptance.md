# Piano di validazione — Team

## Modello di dati
Persona, ruolo, foto, breve biografia.

## Implementazione attesa
Usare il blocco team nativo con foto omogenee e testi forniti dalle persone.

## Test da prevedere
1. Nominale: Visualizzare il team su mobile con testi alternativi corretti.
2. Controllo di rifiuto: Una persona rimossa scompare anche dalle pagine in cache.
3. Invariante: Nessuna foto o informazione pubblicata senza il consenso della persona.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
