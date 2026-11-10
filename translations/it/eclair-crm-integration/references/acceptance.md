# Piano di validazione — Sincronizzazione CRM

## Modello di dati
Contatto, azienda, consenso, mapping, chiave esterna, provenienza.

## Implementazione attesa
Mappare campi rigorosi, differenziare aggiornamenti direzionali e fusione, fornire riconciliazione ed esportazione/eliminazione.

## Test da prevedere
1. Nominale: Testare fusione, email modificata, conflitto, eliminazione e ripresa.
2. Controllo di rifiuto: Lo stesso contatto risincronizzato non crea più duplicati nel CRM.
3. Invariante: Non esportare contatti senza base giuridica né scope minimi.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
