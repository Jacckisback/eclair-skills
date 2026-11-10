# Piano di validazione — Video

## Modello di dati
Video, sorgente, immagine di anteprima, sottotitoli.

## Implementazione attesa
Usare il blocco video nativo, preferire una facciata cliccabile per le piattaforme di terze parti, fornire sottotitoli o trascrizione.

## Test da prevedere
1. Nominale: Verificare che nessuna richiesta verso terze parti parta prima del clic.
2. Controllo di rifiuto: Un indirizzo video di un dominio non autorizzato viene rifiutato.
3. Invariante: Nessun player di terze parti viene caricato prima del clic del visitatore.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
