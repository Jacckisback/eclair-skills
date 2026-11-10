# Piano di validazione — Caricamento differito

## Modello di dati
Immagine, priorità, dimensioni.

## Implementazione attesa
Verificare che l'immagine principale sia caricata con priorità e le altre in differita, con dimensioni esplicite.

## Test da prevedere
1. Nominale: Misurare la visualizzazione dell'elemento più grande e lo spostamento del layout.
2. Controllo di rifiuto: L'immagine principale non viene mai caricata in differita.
3. Invariante: Nessuno script di terze parti viene aggiunto per differire il caricamento.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
