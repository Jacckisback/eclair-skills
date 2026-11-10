# Piano di validazione — Aggiornamenti e rollback

## Modello di dati
Versione installata, versione annunciata, firma, punto di ripristino.

## Implementazione attesa
Eseguire il backup, leggere le note di rilascio, avviare l'aggiornamento con un clic, verificare il sito, saper tornare alla versione precedente.

## Test da prevedere
1. Nominale: Aggiornare una copia del sito e poi tornare indietro.
2. Controllo di rifiuto: Un annuncio di aggiornamento non firmato dal maintainer viene rifiutato.
3. Invariante: Non installare mai un archivio la cui firma non sia verificata dal core.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
