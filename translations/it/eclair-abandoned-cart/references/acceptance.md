# Piano di validazione — Recupero del carrello abbandonato

## Modello di dati
Carrello, contatto, consenso, sollecito.

## Implementazione attesa
Verificare la base giuridica, limitare il numero di solleciti, basarsi sugli strumenti del fornitore di pagamento quando esistono.

## Test da prevedere
1. Nominale: Simulare abbandono, sollecito e disiscrizione.
2. Controllo di rifiuto: Un contatto disiscritto non riceve alcun sollecito.
3. Invariante: Nessun sollecito senza consenso o base giuridica; disiscrizione immediata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
