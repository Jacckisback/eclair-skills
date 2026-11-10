# Piano di validazione — Appuntamenti e calendario

## Modello di dati
Fornitore del servizio, servizio, durata, buffer, eccezioni, eventi e fusi orari.

## Implementazione attesa
Normalizzare gli orari in UTC, conservare il fuso orario di visualizzazione, bloccare le fasce di indisponibilità, gestire la risincronizzazione esterna.

## Test da prevedere
1. Nominale: Testare DST, appuntamento a cavallo della mezzanotte, evento eliminato.
2. Controllo di rifiuto: Una fascia oraria bloccata manualmente non viene mai proposta dopo la risincronizzazione.
3. Invariante: Un'integrazione esterna richiede OAuth/scope minimi e non deve esporre i calendari privati.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
