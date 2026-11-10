# Piano di validazione — Linee del tempo

## Modello di dati
Tappa, data, titolo, testo.

## Implementazione attesa
Rendere la linea del tempo come elenco ordinato stilizzato in CSS, leggibile in colonna su mobile.

## Test da prevedere
1. Nominale: Verificare l'ordine di lettura e la visualizzazione su mobile.
2. Controllo di rifiuto: Una tappa senza data resta leggibile e ordinata.
3. Invariante: Le date e i fatti visualizzati sono forniti dal cliente.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
