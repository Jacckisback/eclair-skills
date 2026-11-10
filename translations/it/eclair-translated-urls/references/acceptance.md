# Piano di validazione — Indirizzi tradotti

## Modello di dati
Indirizzo per lingua, reindirizzamenti, canonical, hreflang.

## Implementazione attesa
Fissare una convenzione di indirizzi per lingua, tradurre gli slug prima della pubblicazione, verificare canonical e hreflang prodotti dal core.

## Test da prevedere
1. Nominale: Verificare canonical e hreflang di ogni versione.
2. Controllo di rifiuto: Due lingue non condividono mai lo stesso indirizzo.
3. Invariante: Nessun indirizzo pubblicato viene cambiato senza reindirizzamento.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
