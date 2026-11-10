# Piano di validazione — Backup e ripristino

## Modello di dati
Archivio di backup, data, destinazione, test di ripristino.

## Implementazione attesa
Attivare il backup scaricabile o verso lo storage remoto previsto dal core, fissare la frequenza, ripristinare su una copia per verificare.

## Test da prevedere
1. Nominale: Ripristinare l'ultimo backup su un'installazione di test e confrontare.
2. Controllo di rifiuto: Un archivio modificato o manomesso viene rifiutato al ripristino.
3. Invariante: Un backup contiene dati personali: viene conservato cifrato o in un luogo sicuro, mai in una cartella pubblica.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
