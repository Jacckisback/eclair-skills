# Piano di validazione — Sblocco progressivo

## Modello di dati
Lezione, regola di sblocco, data o condizione, iscritto.

## Implementazione attesa
Descrivere le regole (data, intervallo dopo l'iscrizione, lezione precedente), applicarle lato server a ogni richiesta.

## Test da prevedere
1. Nominale: Simulare il trascorrere del tempo e il completamento di una lezione.
2. Controllo di rifiuto: Un indirizzo di lezione bloccata indovinato non restituisce il suo contenuto.
3. Invariante: Una lezione bloccata non viene mai inviata al browser, nemmeno nascosta.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
