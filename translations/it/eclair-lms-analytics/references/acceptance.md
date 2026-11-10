# Piano di validazione — Cruscotto didattico

## Modello di dati
Iscrizioni, progressi, risultati aggregati, eventi dei corsi.

## Implementazione attesa
Definire metriche utili ai formatori, filtrare per corso e autorizzazione; ridurre la raccolta; prevedere conservazione ed esportazione.

## Test da prevedere
1. Nominale: Testare la visibilità del formatore sul corso A vs B.
2. Controllo di rifiuto: Una richiesta di statistiche aggregate non deve esporre l'identità di uno studente terzo.
3. Invariante: Le statistiche di un allievo sono visibili soltanto alle parti autorizzate.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
