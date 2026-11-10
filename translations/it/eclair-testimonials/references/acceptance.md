# Piano di validazione — Testimonianze e recensioni

## Modello di dati
Testimonianza, autore, data, autorizzazione.

## Implementazione attesa
Raccogliere le testimonianze reali con autorizzazione scritta, presentarle come citazioni, indicare la fonte.

## Test da prevedere
1. Nominale: Verificare che ogni testimonianza pubblicata abbia un'autorizzazione registrata.
2. Controllo di rifiuto: Una recensione senza fonte verificabile non viene pubblicata.
3. Invariante: Nessuna recensione inventata, modificata o selezionata in modo ingannevole.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
