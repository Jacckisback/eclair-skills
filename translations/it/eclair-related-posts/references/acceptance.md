# Piano di validazione — Contenuti correlati

## Modello di dati
Contenuto, categoria, parole in comune, elenco di link calcolato.

## Implementazione attesa
Calcolare le correlazioni alla pubblicazione o tramite attività, renderle con un blocco statico memorizzabile in cache, limitarsi a pochi link.

## Test da prevedere
1. Nominale: Verificare i link proposti su più articoli di categorie diverse.
2. Controllo di rifiuto: Un articolo eliminato non viene più proposto dopo la rigenerazione.
3. Invariante: Nessuna correlazione punta a un contenuto non pubblicato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
