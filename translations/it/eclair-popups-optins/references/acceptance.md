# Piano di validazione — Finestre e riquadri di invito

## Modello di dati
Messaggio, attivatore, frequenza, azione.

## Implementazione attesa
Preferire un riquadro nella pagina ; altrimenti dialog nativo attivato da un'azione del visitatore, chiudibile da tastiera, mai all'arrivo.

## Test da prevedere
1. Nominale: Aprire e chiudere da tastiera e su mobile.
2. Controllo di rifiuto: Il riquadro rifiutato non ricompare durante la visita.
3. Invariante: Nessuna finestra blocca il contenuto né intrappola il focus.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
