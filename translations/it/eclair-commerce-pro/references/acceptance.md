# Piano di validazione — Architettura Commerce Pro

## Modello di dati
Catalogo, carrello, prezzi bloccati per riga, ordine, pagamento, rimborso, stock, fattura e registro degli stati.

## Implementazione attesa
Disegnare una macchina a stati ordine/payment, separare lettura pubblica e scritture private, scegliere un'archiviazione transazionale, formalizzare il connettore PSP; identificare i punti non forniti da Éclair v2.

## Test da prevedere
1. Nominale: Simulare acquisto, conferma tramite webhook, nuovo tentativo, rimborso, stock e annullamento.
2. Controllo di rifiuto: Stessa notifica di pagamento consegnata due volte => una sola transizione dell'ordine.
3. Invariante: Nessun pagamento viene dichiarato riuscito in base al solo reindirizzamento del browser; il server valida un evento PSP autenticato.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
