# Piano di validazione — Messaggistica privata

## Modello di dati
Conversazione, partecipanti, messaggio, segnalazione.

## Implementazione attesa
Definire blocco, segnalazione, limiti di invio e conservazione; nessuna conversazione in una pagina in cache.

## Test da prevedere
1. Nominale: Simulare scambio, blocco e segnalazione.
2. Controllo di rifiuto: Un membro bloccato non può più scrivere a chi lo ha bloccato.
3. Invariante: Un messaggio è leggibile soltanto dai suoi partecipanti.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
