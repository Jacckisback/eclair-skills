# Piano di validazione — Servizi di email marketing

## Modello di dati
Lista, modulo ospitato, chiave API, sincronizzazione.

## Implementazione attesa
Usare il modulo ospitato dal servizio; riporre ogni chiave API nei segreti dell'estensione; sincronizzare tramite task se necessario.

## Test da prevedere
1. Nominale: Iscrivere un indirizzo di test e ritrovarlo nel servizio.
2. Controllo di rifiuto: Una chiave revocata produce un errore registrato nei log, non una fuga di dati.
3. Invariante: Nessuna chiave API nel codice, nel repository o in una pagina pubblica.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
