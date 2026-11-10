# Piano di validazione — Argomenti e risposte

## Modello di dati
Argomento, risposta, versione, autore, data e ora, in evidenza, chiuso, eliminato.

## Implementazione attesa
Definire la gerarchia delle risposte, la paginazione, la cronologia delle modifiche, le menzioni e i permalink; gestire invii idempotenti.

## Test da prevedere
1. Nominale: Testare risposte concorrenti, messaggio cancellato e argomento chiuso.
2. Controllo di rifiuto: Un membro non può modificare né eliminare la risposta di un altro senza un permesso esplicito.
3. Invariante: Eseguire l'escape di Markdown/HTML e verificare il permesso di modifica per ogni pubblicazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
