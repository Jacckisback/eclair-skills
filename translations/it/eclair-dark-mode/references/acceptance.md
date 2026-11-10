# Piano di validazione — Modalità scura

## Modello di dati
Set di colori chiaro e scuro, preferenza del visitatore.

## Implementazione attesa
Definire le variabili di colore del tema per prefers-color-scheme, verificare contrasti, immagini e loghi.

## Test da prevedere
1. Nominale: Controllare i contrasti delle due modalità sulle pagine tipo.
2. Controllo di rifiuto: Un logo scuro non diventa invisibile in modalità scura.
3. Invariante: Non serve alcun cookie per rispettare la preferenza di sistema.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
