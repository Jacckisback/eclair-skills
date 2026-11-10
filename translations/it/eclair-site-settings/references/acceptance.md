# Piano di validazione — Impostazioni del sito

## Modello di dati
Nome, descrizione, logo, recapiti, lingua, tema, direzione artistica.

## Implementazione attesa
Leggere le capacità del sito, compilare le impostazioni tramite l'amministrazione, visualizzare l'anteprima prima di salvare.

## Test da prevedere
1. Nominale: Configurare un sito nuovo e verificare la resa pubblica.
2. Controllo di rifiuto: Un account senza permesso Impostazioni non modifica alcuna impostazione.
3. Invariante: Nessuna protezione nativa viene disattivata per guadagnare tempo.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
