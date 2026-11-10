# Piano di validazione — Sezioni di apertura

## Modello di dati
Titolo, sottotitolo, immagine, pulsante.

## Implementazione attesa
Scrivere una promessa precisa, scegliere un'immagine leggera, mantenere un solo titolo principale e un pulsante.

## Test da prevedere
1. Nominale: Misurare la visualizzazione dell'elemento più grande su mobile.
2. Controllo di rifiuto: Senza immagine, la sezione resta leggibile e contrastata.
3. Invariante: L'immagine principale ha dimensioni esplicite e non ritarda la visualizzazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
