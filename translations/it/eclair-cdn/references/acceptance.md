# Piano di validazione — Rete di distribuzione (CDN)

## Modello di dati
Zona DNS, regole di cache, svuotamento.

## Implementazione attesa
Configurare DNS e HTTPS end-to-end, escludere l'amministrazione dalla cache del CDN, definire lo svuotamento alla pubblicazione.

## Test da prevedere
1. Nominale: Verificare gli header di cache delle pagine pubbliche e dell'amministrazione.
2. Controllo di rifiuto: Dopo una modifica, la vecchia versione non viene più servita una volta eseguito lo svuotamento.
3. Invariante: L'amministrazione e qualsiasi risposta privata non vengono mai messe in cache dal CDN.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
