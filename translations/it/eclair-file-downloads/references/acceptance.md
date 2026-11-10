# Piano di validazione — Download

## Modello di dati
File, titolo, versione, dimensione, pagina che lo ospita.

## Implementazione attesa
Collocare i file pubblici nella libreria multimediale, mostrare peso e formato, versionare i file sostituiti.

## Test da prevedere
1. Nominale: Scaricare ogni file e verificare tipo e dimensione dichiarati.
2. Controllo di rifiuto: Un file sostituito non lascia la vecchia versione accessibile per errore.
3. Invariante: Nessun file privato o a pagamento viene collocato a un indirizzo pubblico indovinabile.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
