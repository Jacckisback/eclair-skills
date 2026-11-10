# Piano di validazione — Breadcrumb

## Modello di dati
Livelli, etichette, indirizzi.

## Implementazione attesa
Controllare la coerenza tra struttura ad albero, breadcrumb visualizzato e dati strutturati del core.

## Test da prevedere
1. Nominale: Confrontare breadcrumb visualizzato e markup su tre livelli di profondità.
2. Controllo di rifiuto: Una pagina orfana non mostra un breadcrumb incoerente.
3. Invariante: Il breadcrumb non rivela alcuna pagina non pubblicata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
