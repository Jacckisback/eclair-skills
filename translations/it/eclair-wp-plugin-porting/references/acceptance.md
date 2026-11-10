# Piano di validazione — Porting di plugin WordPress

## Modello di dati
Plugin di origine, funzionalità realmente utilizzate, equivalente nativo, scostamento.

## Implementazione attesa
Elencare ciò che il plugin fa davvero sul sito, cercare prima la funzionalità nativa, altrimenti lo skill del catalogo, altrimenti un'estensione su misura; non copiare mai codice PHP WordPress.

## Test da prevedere
1. Nominale: Redigere la tabella di corrispondenza di un sito reale e farla convalidare.
2. Controllo di rifiuto: Una funzionalità senza equivalente viene dichiarata mancante, non simulata.
3. Invariante: Nessun codice con licenza incompatibile o dipendente dall'API WordPress viene ripreso.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
