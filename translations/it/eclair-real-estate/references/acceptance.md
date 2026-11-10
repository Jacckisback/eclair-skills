# Piano di validazione — Annunci immobiliari

## Modello di dati
Immobile, transazione, geolocalizzazione arrotondata, superficie, media, prezzo, disponibilità.

## Implementazione attesa
Versionare gli annunci, fornire filtri limitati, gestire lo stato venduto/affittato, le immagini e le richieste di visita.

## Test da prevedere
1. Nominale: Testare annunci ritirati, media privati e filtri.
2. Controllo di rifiuto: Un immobile eliminato smette di comparire nei risultati e nella cache dopo lo svuotamento.
3. Invariante: Non esporre indirizzi esatti o recapiti dei proprietari senza finalità e autorizzazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
