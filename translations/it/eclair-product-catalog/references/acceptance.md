# Piano di validazione — Catalogo prodotti

## Modello di dati
Prodotto, SKU, slug, titolo, descrizione, prezzo di presentazione, media, disponibilità e categoria.

## Implementazione attesa
Prototipare prima una pagina pubblica GET memorizzabile in cache; produrre uno schema prodotto e il relativo indice; mantenere titoli e descrizioni sorgente; definire paginazione e canonical; preservare gli slug nel corso delle modifiche.

## Test da prevedere
1. Nominale: Testare categorie, elenchi vuoti, URL canonico, ricerca ed eliminazione soft.
2. Controllo di rifiuto: Un prodotto eliminato o privato non deve restare nel catalogo né in una vecchia cache.
3. Invariante: Il prezzo visualizzato non viene mai assunto come fonte autorevole per un futuro ordine.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
