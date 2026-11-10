# Piano di validazione — Media didattici

## Modello di dati
Lezione, media, trascrizione, file scaricabili, permessi e durata.

## Implementazione attesa
Preparare media e sottotitoli accessibili; prevedere una distribuzione con autorizzazione lato server o URL firmato di breve durata; separare CDN pubblico e contenuto riservato.

## Test da prevedere
1. Nominale: Testare media scaduto, accesso senza iscrizione e mobile.
2. Controllo di rifiuto: Un URL di documento privato copiato in un altro browser viene rifiutato o scade.
3. Invariante: Nascondere un link nell'HTML non è una protezione; non collocare il media privato in /media pubblico.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
