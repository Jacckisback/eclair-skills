# Piano di validazione — Account dei clienti

## Modello di dati
Cliente, credenziali, ordini, indirizzi.

## Implementazione attesa
Definire registrazione, accesso, recupero ed eliminazione dell'account; separare rigorosamente account dei clienti e account di amministrazione.

## Test da prevedere
1. Nominale: Simulare registrazione, accesso, consultazione ed eliminazione dell'account.
2. Controllo di rifiuto: Un cliente non può leggere l'ordine di un altro cambiando un identificativo.
3. Invariante: Un cliente vede soltanto i propri dati; mai cache condivisa sull'area clienti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
