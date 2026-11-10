# Piano di validazione — Test A/B

## Modello di dati
Variante, ripartizione, obiettivo, risultato.

## Implementazione attesa
Testare per periodi successivi o con indirizzi distinti anziché con varianti nella cache ; fissare in anticipo ipotesi, durata e misura.

## Test da prevedere
1. Nominale: Svolgere un test su due landing page distinte.
2. Controllo di rifiuto: Un risultato senza volume sufficiente non viene presentato come conclusivo.
3. Invariante: Nessuna variante viene archiviata nella cache condivisa in funzione del visitatore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
