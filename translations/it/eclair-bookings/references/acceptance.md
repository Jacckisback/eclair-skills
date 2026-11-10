# Piano di validazione — Prenotazioni per attività professionali

## Modello di dati
Risorsa, fascia oraria, capienza, fuso orario, stato e prenotazione.

## Implementazione attesa
Definire le regole di disponibilità e di annullamento, bloccare le fasce orarie in modo transazionale, distinguere opzione e prenotazione confermata.

## Test da prevedere
1. Nominale: Testare clienti simultanei, cambi d'ora e annullamento.
2. Controllo di rifiuto: Ultimo posto prenotato simultaneamente => una sola conferma.
3. Invariante: Nessun calendario GET in cache sostituisce la convalida transazionale della disponibilità.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
