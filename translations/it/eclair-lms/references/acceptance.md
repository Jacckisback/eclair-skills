# Piano di validazione — Architettura LMS

## Modello di dati
Corsi, sezioni, lezioni, prerequisiti, iscrizioni, progressi, permessi ed eventuali vendite.

## Implementazione attesa
Definire cataloghi pubblici vs lezioni private; scegliere un salvataggio dei progressi transazionale; collegare l'accesso all'identità verificata del membro; comporre moduli indipendenti.

## Test da prevedere
1. Nominale: Testare studente, docente, amministratore e visitatore.
2. Controllo di rifiuto: Un allievo iscritto non può leggere il contenuto privato di un altro corso.
3. Invariante: Nessuna promessa di accesso privato tramite un semplice URL segreto o un blocco nascosto.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
