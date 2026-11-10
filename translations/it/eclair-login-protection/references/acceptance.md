# Piano di validazione — Protezione dell'accesso

## Modello di dati
Tentativi, limiti per rete e per account, indirizzo dell'amministrazione.

## Implementazione attesa
Controllare i limiti nativi dei tentativi, l'indirizzo dell'amministrazione, le sessioni attive e le password provvisorie.

## Test da prevedere
1. Nominale: Simulare errori ripetuti e constatare il blocco.
2. Controllo di rifiuto: Il dispositivo abituale del proprietario non viene bloccato dai tentativi di un terzo.
3. Invariante: Nessun limite nativo viene allentato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
