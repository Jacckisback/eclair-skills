# Piano di validazione — Workflow IA

## Modello di dati
Bozza, proposta, convalida, modello, costo, fonte e audit.

## Implementazione attesa
Usare le capacità MCP del core, mantenere una persona nel ciclo decisionale, limitare accesso e budget; valutare qualità e allucinazioni.

## Test da prevedere
1. Nominale: Testare prompt injection, cambio di contesto e rollback.
2. Controllo di rifiuto: Un'istruzione ostile in un articolo importato non diventa un comando eseguito.
3. Invariante: Nessuna IA pubblica, distribuisce, elimina o modifica del PHP direttamente tramite MCP senza controllo.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
