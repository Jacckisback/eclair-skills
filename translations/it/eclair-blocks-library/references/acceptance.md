# Piano di validazione — Libreria di blocchi

## Modello di dati
Tipo con namespace, dichiarazione dei campi, limiti, resa e dati conservati.

## Implementazione attesa
Privilegiare i blocchi nativi; dichiarare i campi autorizzati; generare resa con escaping, valori predefiniti e conservazione dopo la disattivazione.

## Test da prevedere
1. Nominale: Testare campi non validi, rimozione dell'estensione e reinstallazione.
2. Controllo di rifiuto: Il blocco disattivato viene conservato ma non viene né eseguito né reso.
3. Invariante: Rifiutare l'esecuzione di HTML/JS proveniente dai campi; nessuna perdita di dati quando il blocco manca.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
