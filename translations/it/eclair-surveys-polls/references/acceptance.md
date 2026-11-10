# Piano di validazione — Sondaggi e indagini

## Modello di dati
Domanda, scelte, risposta, partecipante anonimo, risultati aggregati.

## Implementazione attesa
Definire anonimato, limitazione dei voti multipli, visualizzazione dei risultati aggregati e durata del sondaggio.

## Test da prevedere
1. Nominale: Votare, consultare i risultati e chiudere il sondaggio.
2. Controllo di rifiuto: Un secondo voto dello stesso partecipante viene ignorato.
3. Invariante: Nessuna risposta individuale viene pubblicata ; soltanto risultati aggregati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
