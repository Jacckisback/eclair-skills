# Piano di validazione — Segnali web essenziali

## Modello di dati
Visualizzazione dell'elemento più grande, stabilità, reattività, per template.

## Implementazione attesa
Misurare in laboratorio e su dati reali quando esistono, trattare la causa principale per template, misurare di nuovo.

## Test da prevedere
1. Nominale: Misurare tre template su mobile prima e dopo la correzione.
2. Controllo di rifiuto: Un miglioramento non misurato non viene annunciato come acquisito.
3. Invariante: Nessun punteggio viene promesso; vengono riportati soltanto i risultati misurati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
