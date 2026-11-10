# Piano di validazione — GEO e agenti IA

## Modello di dati
Contenuto verificabile, provenienza, semantica, llms.txt, Markdown, Schema.org.

## Implementazione attesa
Sottoporre ad audit struttura, risposte fattuali, fonti e coerenza del Markdown; controllare i robot IA senza promesse eccessive.

## Test da prevedere
1. Nominale: Testare versione Markdown, citazioni strutturate e robots.txt.
2. Controllo di rifiuto: I fatti mostrati a robot e a esseri umani restano coerenti e aggiornati.
3. Invariante: Non confondere punteggio GEO interno, citabilità e posizionamento garantito.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
