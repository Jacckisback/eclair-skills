# Piano di validazione — Protezione dallo spam

## Modello di dati
Messaggio, token del modulo, limite di frequenza.

## Implementazione attesa
Basarsi sul token e sui limiti del modulo nativo, aggiungere se necessario un campo trappola, sorvegliare la casella di posta in arrivo.

## Test da prevedere
1. Nominale: Inviare un messaggio legittimo e poi una raffica automatizzata.
2. Controllo di rifiuto: Un invio senza token valido viene respinto.
3. Invariante: Nessun servizio di terze parti riceve i messaggi dei visitatori senza informazione preventiva.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
