# Piano di validazione — Feed dei social network

## Modello di dati
Pubblicazione, immagine, link, data di recupero.

## Implementazione attesa
Recuperare le pubblicazioni tramite attività pianificata lato server quando il social network lo consente, renderle in HTML statico ; altrimenti semplici link ai profili.

## Test da prevedere
1. Nominale: Verificare la resa statica e l'aggiornamento tramite attività.
2. Controllo di rifiuto: Se il social network non è disponibile, resta visualizzata l'ultima versione valida.
3. Invariante: Nessun widget di terze parti viene caricato nel browser dei visitatori.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
