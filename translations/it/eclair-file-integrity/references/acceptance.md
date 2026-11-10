# Piano di validazione — Integrità dei file

## Modello di dati
File, impronta attesa, scostamento.

## Implementazione attesa
Avviare il controllo di integrità dalla pagina Sicurezza, spiegare ogni scostamento, ripristinare i file originali se necessario.

## Test da prevedere
1. Nominale: Modificare un file su una copia di test e constatare l'avviso.
2. Controllo di rifiuto: Un file del core alterato non viene mai dichiarato conforme.
3. Invariante: Uno scostamento inspiegato viene trattato come un incidente, non ignorato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
