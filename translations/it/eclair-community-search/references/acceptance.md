# Piano di validazione — Ricerca nel forum

## Modello di dati
Termine, indice limitato, lingua, categoria, pagina, stato e permessi.

## Implementazione attesa
Normalizzare il testo, indicizzare le pubblicazioni autorizzate, paginare e limitare il costo, rimuovere dai risultati gli oggetti eliminati.

## Test da prevedere
1. Nominale: Testare frase vuota, injection, ricerca massiva, argomenti privati.
2. Controllo di rifiuto: Un visitatore non deve vedere l'estratto di una discussione privata in un suggerimento.
3. Invariante: Il filtro dei permessi interviene a ogni ricerca, non soltanto al momento dell'indicizzazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
