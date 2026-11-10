# Piano di validazione — Articoli del blog

## Modello di dati
Articolo, estratto, immagine principale, categoria, autore, data, stato bozza o pubblicato.

## Implementazione attesa
Creare gli articoli in bozza dall'amministrazione o dal connettore MCP, verificare titolo, estratto, immagine e categoria, poi lasciare che sia una persona a pubblicare.

## Test da prevedere
1. Nominale: Creare una bozza completa, farla pubblicare, poi verificarne la resa, il feed RSS e la sitemap.
2. Controllo di rifiuto: Una bozza non compare né sul sito pubblico, né nella sitemap, né nel feed.
3. Invariante: Non pubblicare né eliminare mai un contenuto al posto della persona autorizzata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
