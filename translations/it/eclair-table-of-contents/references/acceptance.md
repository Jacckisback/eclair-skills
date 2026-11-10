# Piano di validazione — Sommario automatico

## Modello di dati
Titoli di sezione, ancore, livelli.

## Implementazione attesa
Generare il sommario dai titoli di sezione durante il rendering lato server, con ancore stabili e senza JavaScript obbligatorio.

## Test da prevedere
1. Nominale: Verificare il sommario su un contenuto con tre livelli di titoli di sezione.
2. Controllo di rifiuto: Un contenuto breve senza titoli di sezione non mostra alcun sommario vuoto.
3. Invariante: Le ancore generate sono sottoposte a escaping e univoche.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
