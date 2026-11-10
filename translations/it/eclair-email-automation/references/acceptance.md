# Piano di validazione — Email transazionali

## Modello di dati
Template, lingua, consenso, destinatario, dominio, evento, consegna.

## Implementazione attesa
Preparare modelli testo/HTML, DKIM/SPF/DMARC e deliverability; distinguere transazionale e marketing, registro senza segreti, disiscrizione obbligatoria.

## Test da prevedere
1. Nominale: Testare errore SMTP, errore di indirizzo, ripresa e scadenza del token.
2. Controllo di rifiuto: Un errore SMTP non contrassegna un'email come consegnata né blocca un account in modo definitivo.
3. Invariante: Non inviare un token di recupero tramite URL non verificato; mai spam senza consenso.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
