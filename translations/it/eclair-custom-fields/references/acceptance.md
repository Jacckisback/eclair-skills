# Piano di validazione — Campi personalizzati

## Modello di dati
Campo, tipo dichiarato, valore validato, blocco o impostazione che lo ospita.

## Implementazione attesa
Dichiarare i campi nel manifesto (tipi supportati dal core), lasciare che il core validi e archivi, rendere con escaping.

## Test da prevedere
1. Nominale: Dichiarare un blocco con campi testo, numero e scelta, poi verificare validazione e resa.
2. Controllo di rifiuto: Un valore fuori formato viene rifiutato dal core e non raggiunge mai la resa.
3. Invariante: Ogni valore visualizzato passa per e() ; nessun campo contiene segreti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
