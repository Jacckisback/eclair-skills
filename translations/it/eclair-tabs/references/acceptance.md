# Piano di validazione — Schede

## Modello di dati
Scheda, titolo, pannello.

## Implementazione attesa
Costruire un blocco di schede con ruoli ARIA, navigazione con i tasti freccia e ripiego in sezioni impilate.

## Test da prevedere
1. Nominale: Percorrere le schede da tastiera e con lo screen reader.
2. Controllo di rifiuto: Senza JavaScript, tutti i pannelli sono visibili.
3. Invariante: Tutto il contenuto resta nell'HTML, quindi leggibile senza JavaScript.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
