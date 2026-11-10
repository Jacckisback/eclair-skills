# Piano di validazione — Lingue da destra a sinistra

## Modello di dati
Direzione del testo, proprietà logiche CSS, icone orientate.

## Implementazione attesa
Usare le proprietà logiche CSS nel tema del sito, testare ogni template in dir=rtl.

## Test da prevedere
1. Nominale: Visualizzare le pagine tipo da destra a sinistra senza overflow.
2. Controllo di rifiuto: Una mescolanza di lingue non compromette l'ordine di lettura.
3. Invariante: Nessun testo dell'utente viene iniettato senza escaping, compresi i caratteri di direzione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
