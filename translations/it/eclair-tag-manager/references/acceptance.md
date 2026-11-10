# Piano di validazione — Gestore di tag

## Modello di dati
Contenitore, tag, attivatori, consenso.

## Implementazione attesa
Elencare i tag realmente necessari, cercare un'alternativa lato server, documentare il blocco da parte della politica dei contenuti nativa.

## Test da prevedere
1. Nominale: Redigere l'inventario dei tag e della loro alternativa.
2. Controllo di rifiuto: Un tag non giustificato non viene aggiunto.
3. Invariante: Nessun contenitore che consenta di iniettare codice arbitrario senza revisione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
