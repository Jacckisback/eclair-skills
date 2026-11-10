# Piano di validazione — Documenti PDF

## Modello di dati
Documento, titolo, riassunto, pagina di presentazione, file.

## Implementazione attesa
Creare una pagina HTML di presentazione per documento con riassunto, link di download e alternativa accessibile.

## Test da prevedere
1. Nominale: Verificare link, peso, titolo del documento e pagina di presentazione.
2. Controllo di rifiuto: Un PDF rimosso restituisce una risposta pulita e non un link rotto nelle pagine.
3. Invariante: Nessun PDF contenente dati personali viene pubblicato senza consenso.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
