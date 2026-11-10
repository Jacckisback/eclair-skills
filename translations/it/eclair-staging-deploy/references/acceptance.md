# Piano di validazione — Staging e messa online

## Modello di dati
Copia di test, differenze, checklist di messa online.

## Implementazione attesa
Ripristinare un backup su un sottodominio protetto e non indicizzabile, convalidarvi tema e funzionalità, poi riprodurre in produzione.

## Test da prevedere
1. Nominale: Seguire un cambio di tema dalla copia alla produzione.
2. Controllo di rifiuto: La copia di test non è né indicizzata né accessibile senza autenticazione.
3. Invariante: La copia di test è protetta da password e bloccata ai bot.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
