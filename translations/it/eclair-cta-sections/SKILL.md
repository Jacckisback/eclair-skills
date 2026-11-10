---
name: eclair-cta-sections
description: "Inserire inviti all'azione chiari con i blocchi nativi. Use on Éclair CMS 2.x when the user wants to: posizionare inviti all'azione chiari con i blocchi nativi. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Inviti all'azione — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **posizionare inviti all'azione chiari con i blocchi nativi**. Questa funzione è **già integrata nel core di Éclair 2.0**: la skill ne guida la configurazione e la verifica, senza scrivere alcuna estensione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Blocchi pulsante e banner di invito all'azione. Famiglia: Blocchi e componenti.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Titolo, testo, pulsante, destinazione**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Definire un'azione principale per pagina, ripeterla nei punti giusti, verificare contrasto ed etichetta esplicita. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** La funzione esiste nel core: configurarla tramite l'amministrazione oppure, in bozza, tramite il connettore MCP. Non duplicarla in un'estensione e non modificare mai il core per adattarla; se un'esigenza va oltre ciò che il core offre, segnalarla come scostamento.
7. **Invariante di sicurezza:** Nessun link ingannevole né reindirizzamento aperto. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Seguire ogni pulsante fino alla sua destinazione su mobile» e il test di rifiuto «Un pulsante senza destinazione valida non viene pubblicato». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Impostazioni e contenuti preparati tramite l'amministrazione o in bozza tramite il MCP; **nessuna estensione** finché il nativo è sufficiente.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Seguire ogni pulsante fino alla sua destinazione su mobile.
- Un pulsante senza destinazione valida non viene pubblicato.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `core-builtin-configuration-workflow`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
