# Piano di validazione — Google Analytics

## Modello di dati
ID di misurazione, consenso, eventi.

## Implementazione attesa
Verificare prima se basta una misurazione senza cookie; altrimenti consenso preventivo, e presa d'atto che la politica dei contenuti nativa non è aperta alle estensioni.

## Test da prevedere
1. Nominale: Verificare l'assenza di richieste prima del consenso.
2. Controllo di rifiuto: Dopo il rifiuto, nessun dato viene inviato.
3. Invariante: Nessuno script di misurazione caricato prima del consenso né aggirando la Content-Security-Policy.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
