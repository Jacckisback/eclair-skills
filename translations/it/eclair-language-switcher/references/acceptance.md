# Piano di validazione — Selettore di lingua

## Modello di dati
Lingua corrente, versioni disponibili, etichette.

## Implementazione attesa
Elencare le lingue con il loro nome nella propria lingua, puntare alla versione equivalente, senza reindirizzamento automatico forzato.

## Test da prevedere
1. Nominale: Cambiare lingua da una pagina profonda e arrivare alla sua equivalente.
2. Controllo di rifiuto: In assenza di equivalente, il link porta alla home della lingua, non a un errore.
3. Invariante: Nessun reindirizzamento in base all'indirizzo IP ; la scelta del visitatore viene rispettata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
