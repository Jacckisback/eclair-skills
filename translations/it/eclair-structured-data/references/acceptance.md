# Piano di validazione — Dati strutturati

## Modello di dati
WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList.

## Implementazione attesa
Ispezionare il JSON-LD nativo prima di aggiungere un tipo; evitare duplicazioni; allineare ogni campo ai dati visibili e alle linee guida dei motori.

## Test da prevedere
1. Nominale: Testare JSON valido, canonical, identificatori e contenuto visualizzato.
2. Controllo di rifiuto: Nessun prezzo/recensione/product inventato o assente dalla pagina figura nel JSON-LD.
3. Invariante: Éclair v2 non espone ancora tutti i contributi JSON-LD alle estensioni; proporre una RFC anziché un'iniezione opaca.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
