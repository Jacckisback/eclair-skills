# Piano di validazione — UX responsive

## Modello di dati
Breakpoint, densità, larghezza del testo, menu, moduli e media.

## Implementazione attesa
Progettare mobile-first; mantenere la gerarchia dell'informazione; testare schermi piccoli, dimensioni dei target e orientamenti.

## Test da prevedere
1. Nominale: Testare 320px, 375px, tablet e tastiera mobile.
2. Controllo di rifiuto: Un'azione primaria resta visibile e utilizzabile su schermo stretto senza scroll orizzontale.
3. Invariante: Nessun contenuto essenziale nascosto su mobile o dipendente da un'animazione.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
