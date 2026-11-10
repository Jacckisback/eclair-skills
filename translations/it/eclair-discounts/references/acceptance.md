# Piano di validazione — Promozioni e coupon

## Modello di dati
Codice, budget, date, quota, condizioni del carrello, utilizzi ed esclusioni.

## Implementazione attesa
Definire ordine di calcolo e arrotondamento; verificare il coupon prima dell'ordine; conteggiare gli utilizzi in modo atomico; tracciare annullamento e reso.

## Test da prevedere
1. Nominale: Testare coupon scaduti, esauriti, soglia ed esclusioni.
2. Controllo di rifiuto: Due ordini simultanei non possono consumare l'ultimo coupon monouso.
3. Invariante: La decisione di idoneità proviene dai dati del server e non dallo sconto inserito nell'HTML.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
