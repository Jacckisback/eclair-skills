# Piano di validazione — Font

## Modello di dati
Font, pesi, file self-hosted, fallback di sistema.

## Implementazione attesa
Usare i font di sistema o il font per i titoli self-hosted delle direzioni artistiche, limitare i pesi.

## Test da prevedere
1. Nominale: Verificare l'assenza di richieste a terze parti e di salti del testo.
2. Controllo di rifiuto: Un font non disponibile lascia un fallback leggibile.
3. Invariante: Nessun font viene caricato da un servizio di terze parti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
