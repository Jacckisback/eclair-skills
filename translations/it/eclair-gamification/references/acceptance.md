# Piano di validazione — Badge e punti

## Modello di dati
Regola, punti, badge, classifica.

## Implementazione attesa
Fissare regole semplici e verificabili lato server, prevedere la revoca in caso di abuso e l'opzione di non comparire in classifica.

## Test da prevedere
1. Nominale: Simulare guadagno, revoca e visualizzazione della classifica.
2. Controllo di rifiuto: Un'azione ripetuta artificialmente non fa guadagnare punti doppi.
3. Invariante: Nessun punto viene attribuito sulla base di un'informazione inviata dal browser.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
