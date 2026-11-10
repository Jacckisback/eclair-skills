# Piano di validazione — Risposta agli incidenti

## Modello di dati
Incidente, cronologia, account coinvolti, backup integro.

## Implementazione attesa
Isolare, conservare le prove, cambiare i segreti, controllare l'integrità, ripristinare un backup integro, informare le persone interessate se necessario.

## Test da prevedere
1. Nominale: Svolgere l'esercitazione su una copia: rilevamento, ripristino, controllo.
2. Controllo di rifiuto: Un sito ripristinato non viene rimesso online prima del cambio di tutti i segreti.
3. Invariante: Non eliminare mai le tracce prima di averle copiate.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
