---
name: eclair-orders-payments
description: "Implementare stati d’ordine e provider di pagamento (PSP) con webhook firmati. Use on Éclair CMS 2.x when the user wants to: implementare gli stati dell'ordine e dei fornitori PSP. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Ordini e pagamenti — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **implementare gli stati dell'ordine e dei fornitori PSP**. Questa funzione **richiede capacità assenti dal core 2.0**: la skill consegna progettazione, mockup sicuro e test, non una messa in produzione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Ordini e gateway di pagamento di WooCommerce. Famiglia: Commerce Pro.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Ordine, tentativo di pagamento, identificativo del fornitore, prova del webhook, idempotency key, rimborso**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Dettagliare le transizioni autorizzate; archiviare la prova della notifica e la sua marca temporale; elaborare i webhook in modo durevole; prevedere reconciliation e rimborso parziale. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Il core fornisce già un negozio leggero (schede prodotto, varianti, categorie, link di pagamento di un fornitore, feed commerciale): usarlo per primo, senza duplicarlo. Oltre a questo, carrello, ordini e pagamenti hanno bisogno di POST pubblici, di uno storage transazionale affidabile, di webhook autenticati e di idempotenza; Éclair 2.0 ufficiale non fornisce tutto questo. La PR #19 è ancora una bozza: non usare mai una route POST non fusa come prova di compatibilità.
7. **Invariante di sicurezza:** Non archiviare mai dati grezzi di carte bancarie; checkout ospitato presso il fornitore e firma dei webhook verificata. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Testare webhook invertito, fuori ordine, riemesso e pagamento rifiutato» e il test di rifiuto «Un webhook senza firma valida non modifica né l'ordine né l'accesso LMS». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Dossier di progettazione, mockup GET sicuro se utile, test bloccanti e richiesta di evoluzione del core; **nessun pacchetto di produzione**.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Testare webhook invertito, fuori ordine, riemesso e pagamento rifiutato.
- Un webhook senza firma valida non modifica né l'ordine né l'accesso LMS.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `design-workflow-requires-verified-core-capabilities`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
