# Piano di validazione — Direzione artistica Éclair

## Modello di dati
Posizionamento, identità, tipografia, colori, componenti, fotografie e contenuto reale.

## Implementazione attesa
Definire un universo ricavato dal mestiere del cliente, comporre sezioni, regolare il CSS e testare i temi con contenuto vero; privilegiare site/themes e i blocchi esistenti.

## Test da prevedere
1. Nominale: Testare contrasto, coerenza tra più pagine e versioni mobile.
2. Controllo di rifiuto: Il nuovo aspetto resta leggibile senza JavaScript e rispetta i link esistenti.
3. Invariante: Non modificare mai app/theme/ né compromettere la SEO, la CSP o il percorso rapido.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
