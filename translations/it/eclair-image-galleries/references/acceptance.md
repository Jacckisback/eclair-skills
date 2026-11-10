# Piano di validazione — Gallerie di immagini

## Modello di dati
Galleria, immagini, didascalie, ordine.

## Implementazione attesa
Comporre la galleria in griglia CSS a partire dalle immagini della libreria multimediale, con didascalie e testi alternativi.

## Test da prevedere
1. Nominale: Visualizzare una galleria di venti immagini su mobile e misurarne il peso.
2. Controllo di rifiuto: Un'immagine rimossa dalla libreria multimediale non lascia una miniatura rotta.
3. Invariante: Nessuna immagine viene caricata da un dominio di terze parti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
