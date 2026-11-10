# Piano di validazione — Registro delle attività

## Modello di dati
Evento, account, data, azione.

## Implementazione attesa
Consultare il registro dalla pagina Sicurezza, individuare accessi e modifiche sensibili, fissare una routine di controllo.

## Test da prevedere
1. Nominale: Provocare un'azione sensibile e ritrovarla nel registro.
2. Controllo di rifiuto: Un account senza permesso Sicurezza non accede al registro.
3. Invariante: Il registro è leggibile soltanto dagli account che hanno il permesso Sicurezza.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
