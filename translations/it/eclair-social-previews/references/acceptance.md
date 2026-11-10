# Piano di validazione — Anteprime di condivisione

## Modello di dati
Titolo di condivisione, descrizione, immagine di condivisione.

## Implementazione attesa
Verificare i tag di condivisione e l'immagine generata dal core, testare l'anteprima sulle principali piattaforme.

## Test da prevedere
1. Nominale: Testare l'anteprima di un articolo e di una pagina.
2. Controllo di rifiuto: Una pagina senza immagine dedicata mantiene un'anteprima predefinita corretta.
3. Invariante: L'immagine di condivisione non contiene alcun dato personale né testo ingannevole.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
