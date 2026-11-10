# Piano di validazione — Script di terze parti

## Modello di dati
Script, finalità, peso, dominio, consenso richiesto.

## Implementazione attesa
Inventariare ogni richiesta di script, cercare un'alternativa senza script, documentare il blocco da parte della politica dei contenuti nativa quando esiste.

## Test da prevedere
1. Nominale: Misurare peso e richieste prima e dopo ogni aggiunta accettata.
2. Controllo di rifiuto: Uno script di un dominio non autorizzato non viene eseguito.
3. Invariante: Nessuno script viene iniettato aggirando la Content-Security-Policy.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
