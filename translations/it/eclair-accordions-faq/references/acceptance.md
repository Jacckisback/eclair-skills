# Piano di validazione — FAQ e accordion

## Modello di dati
Domanda, risposta, ordine.

## Implementazione attesa
Redigere vere domande dei clienti, usare il blocco FAQ nativo che produce anche il markup, limitarne il numero per pagina.

## Test da prevedere
1. Nominale: Verificare apertura da tastiera e markup prodotto.
2. Controllo di rifiuto: Una FAQ vuota non emette alcun markup.
3. Invariante: Nessuna risposta inventata né promessa non verificata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
