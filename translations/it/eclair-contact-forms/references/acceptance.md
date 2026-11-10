# Piano di validazione — Modulo di contatto

## Modello di dati
Messaggio, nome, e-mail, oggetto, data, stato di lettura.

## Implementazione attesa
Inserire il blocco contatto nativo, impostare il destinatario, testare l'invio e la ricezione, mostrare l'informativa.

## Test da prevedere
1. Nominale: Inviare un messaggio reale e ritrovarlo nell'amministrazione e via e-mail.
2. Controllo di rifiuto: Invii ripetuti a raffica vengono limitati dal core.
3. Invariante: I messaggi sono visibili soltanto agli account che hanno il permesso Messages.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
