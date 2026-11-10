# Piano di validazione — Flusso di traduzione

## Modello di dati
Contenuto sorgente, versione di destinazione, traduttore, stato, data di aggiornamento.

## Implementazione attesa
Tenere una tabella dei contenuti da tradurre, produrre le traduzioni in bozza, farle rivedere da un madrelingua, segnalare le versioni obsolete.

## Test da prevedere
1. Nominale: Tradurre una pagina, farla rivedere, pubblicare, poi modificare la sorgente e verificare la segnalazione.
2. Controllo di rifiuto: Una traduzione non rivista resta in bozza.
3. Invariante: Nessuna traduzione giuridica o medica pubblicata senza validazione qualificata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
