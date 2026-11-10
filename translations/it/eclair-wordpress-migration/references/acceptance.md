# Piano di validazione — Migrazione da WordPress

## Modello di dati
Esportazione WordPress, vecchi ID, slug, media, categorie, autori, reindirizzamenti e query ?p=.

## Implementazione attesa
Usare la funzione nativa WordPress; inventariare gli URL storici, simulare l'importazione, confrontare slug/canonical, conservare link esatti e media, fornire un piano di rollback.

## Test da prevedere
1. Nominale: Testare URL con slash finale, query alias, accenti, immagini e pagine eliminate.
2. Controllo di rifiuto: Per ogni vecchio URL indicizzato, ottenere un 200 esatto o un reindirizzamento 301 mirato.
3. Invariante: Evitare 404 ed eliminazioni di URL; mai un cambio DNS senza test e backup.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
