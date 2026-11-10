# Piano di validazione — Loghi di clienti e partner

## Modello di dati
Logo, nome, link facoltativo.

## Implementazione attesa
Mostrare i loghi in griglia statica, dimensioni omogenee, nomi come testo alternativo.

## Test da prevedere
1. Nominale: Verificare la leggibilità in modalità chiara e scura.
2. Controllo di rifiuto: Un logo senza autorizzazione registrata non viene integrato.
3. Invariante: Vengono pubblicati soltanto i loghi il cui uso è autorizzato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
