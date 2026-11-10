---
name: eclair-blog-posts
description: "Pubblicare e organizzare articoli del blog con l'editor a blocchi nativo. Use on Éclair CMS 2.x when the user wants to: pubblicare e organizzare articoli del blog con l'editor a blocchi nativo. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Articoli del blog — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **pubblicare e organizzare articoli del blog con l'editor a blocchi nativo**. Questa funzione è **già integrata nel core di Éclair 2.0**: la skill ne guida la configurazione e la verifica, senza scrivere alcuna estensione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Articoli nativi di WordPress. Famiglia: Contenuti e redazione.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Articolo, estratto, immagine principale, categoria, autore, data, stato bozza o pubblicato**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Creare gli articoli in bozza dall'amministrazione o dal connettore MCP, verificare titolo, estratto, immagine e categoria, poi lasciare che sia una persona a pubblicare. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** La funzione esiste nel core: configurarla tramite l'amministrazione oppure, in bozza, tramite il connettore MCP. Non duplicarla in un'estensione e non modificare mai il core per adattarla; se un'esigenza va oltre ciò che il core offre, segnalarla come scostamento.
7. **Invariante di sicurezza:** Non pubblicare né eliminare mai un contenuto al posto della persona autorizzata. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Creare una bozza completa, farla pubblicare, poi verificarne la resa, il feed RSS e la sitemap» e il test di rifiuto «Una bozza non compare né sul sito pubblico, né nella sitemap, né nel feed». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Impostazioni e contenuti preparati tramite l'amministrazione o in bozza tramite il MCP; **nessuna estensione** finché il nativo è sufficiente.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Creare una bozza completa, farla pubblicare, poi verificarne la resa, il feed RSS e la sitemap.
- Una bozza non compare né sul sito pubblico, né nella sitemap, né nel feed.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `core-builtin-configuration-workflow`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
