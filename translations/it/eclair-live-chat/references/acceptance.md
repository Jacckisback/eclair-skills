# Piano di validazione — Chat in diretta

## Modello di dati
Canale, orari, link di conversazione.

## Implementazione attesa
Preferire un link verso un servizio di messaggistica (WhatsApp, e-mail, telefono) con orari; un widget di terze parti dipende dalla politica dei contenuti nativa.

## Test da prevedere
1. Nominale: Aprire il canale da mobile e da computer.
2. Controllo di rifiuto: Fuori orario, il sito lo comunica invece di promettere una risposta immediata.
3. Invariante: Nessun widget carica tracker prima di un'azione del visitatore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
