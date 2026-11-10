# Piano di validazione — Paginazione ed elenchi

## Modello di dati
Elenco, pagina corrente, dimensione della pagina, link precedente e successivo.

## Implementazione attesa
Fissare una dimensione di pagina ragionevole, indirizzi stabili per pagina e link accessibili.

## Test da prevedere
1. Nominale: Percorrere la prima pagina, una pagina intermedia e l'ultima.
2. Controllo di rifiuto: Un numero di pagina fuori dai limiti risponde con un errore pulito, non con un elenco vuoto indicizzabile.
3. Invariante: I parametri di pagina sono limitati e validati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
