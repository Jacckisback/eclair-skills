# Piano di validazione — Eventi e biglietti

## Modello di dati
Evento, sessione, tipo di posto, prenotazione, biglietto, scansione, rimborso.

## Implementazione attesa
Separare le quote per sessione; emettere biglietti univoci dopo il pagamento confermato; gestire controllo d'ingresso atomico e trasferimento.

## Test da prevedere
1. Nominale: Testare doppia scansione, annullamento e ultimo biglietto simultaneo.
2. Controllo di rifiuto: Stesso biglietto presentato a due ingressi => una sola ammissione accettata.
3. Invariante: Il codice QR non contiene dati personali in chiaro e non autorizza più ingressi.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
