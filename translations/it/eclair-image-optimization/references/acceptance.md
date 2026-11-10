# Piano di validazione — Ottimizzazione delle immagini

## Modello di dati
Immagine sorgente, varianti responsive, dimensioni, peso.

## Implementazione attesa
Fornire sorgenti della giusta dimensione, lasciare che il core produca le varianti, controllare il peso reale servito su mobile.

## Test da prevedere
1. Nominale: Misurare peso e dimensioni serviti su mobile e computer.
2. Controllo di rifiuto: Nessuna immagine viene servita senza dimensioni esplicite.
3. Invariante: I metadati sensibili (geolocalizzazione) non vengono pubblicati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
