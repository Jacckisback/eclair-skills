# Piano di validazione — SEO multilingue

## Modello di dati
Lingua, URL della traduzione, hreflang reciproco, titolo e sitemap.

## Implementazione attesa
Inventariare le lingue pubblicate, definire il mapping delle traduzioni, testare canonical per lingua, hreflang/x-default e assenza di reindirizzamenti invasivi.

## Test da prevedere
1. Nominale: Testare coppie FR/ES/EN, pagine mancanti e cambio di lingua.
2. Controllo di rifiuto: Ogni link hreflang punta a un URL 200 indicizzabile e reciproco.
3. Invariante: Non usare una traduzione automatica non verificata come pagina definitiva.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
