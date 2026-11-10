# Piano di validazione — Slideshow e caroselli

## Modello di dati
Diapositiva, immagine, testo, link, ordine.

## Implementazione attesa
Preferire un'unica immagine forte ; altrimenti scorrimento CSS con comandi da tastiera, pausa e nessuna riproduzione automatica imposta.

## Test da prevedere
1. Nominale: Navigare da tastiera e con lo screen reader, misurare lo spostamento del layout.
2. Controllo di rifiuto: Senza JavaScript, tutto il contenuto delle diapositive resta leggibile.
3. Invariante: Nessuna libreria di terze parti pesante ; rispetto di prefers-reduced-motion.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
