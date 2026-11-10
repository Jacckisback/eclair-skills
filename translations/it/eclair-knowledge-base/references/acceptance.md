# Piano di validazione — Base di conoscenza

## Modello di dati
Articolo di aiuto, sezione, versione, data di aggiornamento.

## Implementazione attesa
Organizzare per problemi degli utenti, una risposta per pagina, navigazione per sezioni e ricerca interna.

## Test da prevedere
1. Nominale: Risolvere tre problemi tipici usando unicamente la documentazione.
2. Controllo di rifiuto: Un articolo obsoleto viene datato e segnalato, non lasciato come valido.
3. Invariante: Nessuna procedura non testata viene pubblicata.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
