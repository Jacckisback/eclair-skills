# Piano di validazione — Pagine del sito

## Modello di dati
Pagina, indirizzo, blocchi, pagina genitore, stato, voce di menu.

## Implementazione attesa
Elencare le pagine necessarie, fissare gli indirizzi prima della redazione, comporre ogni pagina in blocchi e collegare le pagine tra loro.

## Test da prevedere
1. Nominale: Creare la struttura ad albero completa e controllare ogni indirizzo, il menu e il breadcrumb.
2. Controllo di rifiuto: Una pagina rinominata risponde con un unico reindirizzamento 301, mai con un errore 404.
3. Invariante: Non cambiare mai l'indirizzo di una pagina pubblicata senza un reindirizzamento verificato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
