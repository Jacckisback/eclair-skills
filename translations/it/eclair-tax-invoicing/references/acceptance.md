# Piano di validazione — IVA e fatturazione

## Modello di dati
Paese di vendita e di consegna, localizzazione fiscale, aliquota in vigore, fattura, nota di credito, sequenza.

## Implementazione attesa
Elencare giurisdizioni e tipi di clienti; consultare regole aggiornate e consulenza contabile; bloccare base imponibile/aliquota al momento dell'ordine; predisporre esportazioni di fatture e note di credito.

## Test da prevedere
1. Nominale: Testare vendita nazionale, transfrontaliera, rimborso e cambio di aliquota.
2. Controllo di rifiuto: Una fattura emessa e poi annullata non deve essere cancellata né rinumerata silenziosamente.
3. Invariante: Non applicare mai un'aliquota IVA universale né pretendere di garantire la conformità fiscale senza validazione locale.
4. GET/HEAD: cache pubblica solo senza stato di sessione né dati sensibili; canonical, stato HTTP, SEO e GEO invariati o migliorati.
5. POST: mai cache condivisa; CSRF, TLS, permessi, limitazione dei tentativi, idempotenza. Non eseguire se il core non lo supporta ufficialmente.
6. Attivazione e disattivazione: i contenuti sono conservati e le route pubbliche rimosse senza fughe di dati.
7. Controlli: validatore nativo, test PHP e HTTP, budget; registrare i comandi eseguiti, i loro risultati e ciò che non è stato testato.

## Prova di disponibilità
Stato della funzione o dell'estensione, log di CI, matrice dei test, procedura di rollback e rifiuto di qualsiasi promessa non verificata.
