# Piano di validazione — Header di sicurezza

## Modello di dati
Header HTTP, Content-Security-Policy, HTTPS.

## Implementazione attesa
Rilevare gli header serviti, verificare HTTPS ovunque, testare le regole del server web fornite con il core.

## Test da prevedere
1. Nominale: Analizzare gli header di una pagina pubblica e dell'amministrazione.
2. Controllo di rifiuto: Un file sensibile o di dati non viene mai servito dal server web.
3. Invariante: Nessun header di protezione viene rimosso né attenuato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
