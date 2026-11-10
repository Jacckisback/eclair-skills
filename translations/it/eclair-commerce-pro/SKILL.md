---
name: eclair-commerce-pro
description: "Progettare un negozio completo, dal catalogo all’ordine consegnato (punto di ingresso della famiglia). Use on Éclair CMS 2.x when the user wants to: progettare un negozio completo, dal catalogo all'ordine consegnato. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Architettura Commerce Pro — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **progettare un negozio completo, dal catalogo all'ordine consegnato**. Questa funzione **richiede capacità assenti dal core 2.0**: la skill consegna progettazione, mockup sicuro e test, non una messa in produzione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** WooCommerce. Famiglia: Commerce Pro.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Catalogo, carrello, prezzi bloccati per riga, ordine, pagamento, rimborso, stock, fattura e registro degli stati**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Disegnare una macchina a stati ordine/payment, separare lettura pubblica e scritture private, scegliere un'archiviazione transazionale, formalizzare il connettore PSP; identificare i punti non forniti da Éclair v2. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Il core fornisce già un negozio leggero (schede prodotto, varianti, categorie, link di pagamento di un fornitore, feed commerciale): usarlo per primo, senza duplicarlo. Oltre a questo, carrello, ordini e pagamenti hanno bisogno di POST pubblici, di uno storage transazionale affidabile, di webhook autenticati e di idempotenza; Éclair 2.0 ufficiale non fornisce tutto questo. La PR #19 è ancora una bozza: non usare mai una route POST non fusa come prova di compatibilità.
7. **Invariante di sicurezza:** Nessun pagamento viene dichiarato riuscito in base al solo reindirizzamento del browser; il server valida un evento PSP autenticato. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Simulare acquisto, conferma tramite webhook, nuovo tentativo, rimborso, stock e annullamento» e il test di rifiuto «Stessa notifica di pagamento consegnata due volte => una sola transizione dell'ordine». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Dossier di progettazione, mockup GET sicuro se utile, test bloccanti e richiesta di evoluzione del core; **nessun pacchetto di produzione**.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Simulare acquisto, conferma tramite webhook, nuovo tentativo, rimborso, stock e annullamento.
- Stessa notifica di pagamento consegnata due volte => una sola transizione dell'ordine.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `design-workflow-requires-verified-core-capabilities`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
