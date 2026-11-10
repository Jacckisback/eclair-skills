# Piano di validazione — Liste dei desideri

## Modello di dati
Lista, prodotto, proprietario.

## Implementazione attesa
Iniziare con un salvataggio nel browser senza account; progettare la versione con account per un secondo momento.

## Test da prevedere
1. Nominale: Aggiungere, rimuovere e ritrovare dei preferiti.
2. Controllo di rifiuto: Un prodotto eliminato scompare in modo pulito dalle liste.
3. Invariante: Nessuna lista è condivisa o visibile a terzi senza un'azione del proprietario.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
