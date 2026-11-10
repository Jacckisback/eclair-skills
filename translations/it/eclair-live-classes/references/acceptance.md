# Piano di validazione — Lezioni in diretta

## Modello di dati
Sessione, data, fuso orario, link di collegamento, iscritti.

## Implementazione attesa
Pubblicare il calendario delle sessioni in GET, inviare il link di collegamento tramite il servizio di videoconferenza o via e-mail, non su una pagina pubblica.

## Test da prevedere
1. Nominale: Verificare la visualizzazione delle date in due fusi orari.
2. Controllo di rifiuto: Una sessione passata non è più proposta per l'iscrizione.
3. Invariante: Il link di una sessione a pagamento o privata non viene mai pubblicato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
