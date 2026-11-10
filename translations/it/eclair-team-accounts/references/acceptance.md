# Piano di validazione — Account del team

## Modello di dati
Account, permessi, autenticazione a due fattori, ultimo accesso.

## Implementazione attesa
Elencare chi fa che cosa, assegnare i permessi nativi minimi, imporre l'autenticazione a due fattori, rimuovere gli account inutili.

## Test da prevedere
1. Nominale: Creare un account redattore e verificare ciò che può e non può fare.
2. Controllo di rifiuto: Un account senza permesso Impostazioni non può né attivare una funzionalità né cambiare tema.
3. Invariante: Nessun account condiviso; nessun permesso Sicurezza concesso per comodità.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
