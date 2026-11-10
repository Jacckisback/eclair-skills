# Piano di validazione — Flusso editoriale

## Modello di dati
Bozza, autore, revisore, data prevista, stato, voce di pianificazione.

## Implementazione attesa
Stabilire chi redige e chi pubblica secondo i permessi nativi, usare il piano editoriale e le bozze, mantenere una revisione umana prima di ogni messa online.

## Test da prevedere
1. Nominale: Far passare un contenuto dall'idea alla bozza e poi alla pubblicazione da parte di una persona abilitata.
2. Controllo di rifiuto: Un account limitato ai contenuti non può né modificare le impostazioni né pubblicare al posto di un altro ruolo.
3. Invariante: Un agente o un redattore senza permesso di pubblicazione non mette online nulla.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
