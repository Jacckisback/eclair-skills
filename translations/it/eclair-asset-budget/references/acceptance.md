# Piano di validazione — Budget di peso

## Modello di dati
Budget per tipo di risorsa, misura, scostamento.

## Implementazione attesa
Fissare budget per pagina tipo, misurare con lo strumento del core, rifiutare qualsiasi aggiunta che li superi senza giustificazione.

## Test da prevedere
1. Nominale: Avviare la misura dei budget sul sito e sul pacchetto prodotto.
2. Controllo di rifiuto: Un pacchetto che supera il budget non viene consegnato così com'è.
3. Invariante: Nessuna dipendenza di terze parti caricata per una funzione decorativa.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
