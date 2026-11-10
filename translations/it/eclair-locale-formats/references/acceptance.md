# Piano di validazione — Formati regionali

## Modello di dati
Lingua, paese, valuta, fuso orario.

## Implementazione attesa
Centralizzare la formattazione lato server, non scrivere mai un formato fisso nel codice dei template.

## Test da prevedere
1. Nominale: Confrontare una data e un prezzo in francese, inglese e tedesco.
2. Controllo di rifiuto: Una valuta sconosciuta non viene visualizzata con un simbolo predefinito ingannevole.
3. Invariante: Un prezzo visualizzato corrisponde sempre alla valuta realmente fatturata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
