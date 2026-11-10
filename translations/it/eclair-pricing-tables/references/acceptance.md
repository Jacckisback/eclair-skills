# Piano di validazione — Tabelle dei prezzi

## Modello di dati
Offerta, prezzo, periodo, caratteristiche, pulsante.

## Implementazione attesa
Comporre le offerte in schede confrontabili, mostrare i prezzi IVA inclusa o IVA esclusa senza ambiguità e collegare ogni pulsante all'azione corretta.

## Test da prevedere
1. Nominale: Confrontare tre offerte su mobile e verificare ogni link.
2. Controllo di rifiuto: Un'offerta senza prezzo validato non viene visualizzata.
3. Invariante: Nessun prezzo, sconto o nota legale inventati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
