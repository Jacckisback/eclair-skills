# Piano di validazione — Intestazioni e piè di pagina

## Modello di dati
Logo, menu, recapiti, link legali.

## Implementazione attesa
Passare per un pacchetto di tema in site/themes, rispettare le variabili del contratto di tema, mantenere link di salto al contenuto e link legali.

## Test da prevedere
1. Nominale: Validare il tema e verificare intestazione e piè di pagina su tutte le pagine tipo.
2. Controllo di rifiuto: Il tema rifiutato dal validatore non viene consegnato.
3. Invariante: Non generare mai in proprio tag SEO o intestazioni già forniti dal core.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
