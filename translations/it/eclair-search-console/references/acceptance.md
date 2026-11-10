# Piano di validazione — Search Console

## Modello di dati
Proprietà, metodo di verifica, sitemap dichiarata, report.

## Implementazione attesa
Verificare il dominio tramite record DNS, dichiarare la sitemap nativa, leggere copertura e query ogni mese.

## Test da prevedere
1. Nominale: Verificare la proprietà e la presa in carico della sitemap.
2. Controllo di rifiuto: Un errore di copertura viene spiegato, non nascosto.
3. Invariante: Nessun accesso da proprietario concesso a terzi senza l'accordo del cliente.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
