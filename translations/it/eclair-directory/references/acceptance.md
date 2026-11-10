# Piano di validazione — Elenco di professionisti

## Modello di dati
Scheda, categoria, località, contatto pubblico, stato di verifica.

## Implementazione attesa
Separare dati professionali pubblici e privati; creare pagine di categoria, canonical, moderazione e filtri limitati.

## Test da prevedere
1. Nominale: Testare schede false, duplicati, eliminazione e ricerca vuota.
2. Controllo di rifiuto: Una scheda in attesa non compare né nella sitemap né nei dati strutturati.
3. Invariante: Non pubblicare indirizzo personale, telefono o recapiti sensibili senza autorizzazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
