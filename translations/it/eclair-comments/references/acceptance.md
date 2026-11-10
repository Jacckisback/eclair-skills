# Piano di validazione — Commenti

## Modello di dati
Commento, autore, stato di moderazione, articolo, data.

## Implementazione attesa
Definire coda di moderazione, regole antispam, note legali e visualizzazione in cache ; proporre nel frattempo un servizio esterno o un contatto diretto.

## Test da prevedere
1. Nominale: Simulare invio, moderazione, pubblicazione ed eliminazione di un commento.
2. Controllo di rifiuto: Un commento in attesa o rifiutato non compare mai in una pagina in cache.
3. Invariante: Nessun commento viene visualizzato senza moderazione ; nessun indirizzo e-mail viene reso pubblico.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
