---
name: eclair-pdf-documents
description: "Pubblicare PDF leggibili, accessibili e indicizzati. Use on Éclair CMS 2.x when the user wants to: pubblicare PDF leggibili, accessibili e indicizzati. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Documenti PDF — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **pubblicare PDF leggibili, accessibili e indicizzati**. Questa funzione è **realizzabile oggi** con il contratto nativo (tema, blocchi, route GET, pagine di amministrazione, task). Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** PDF Embedder, visualizzatori di documenti. Famiglia: Media.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Documento, titolo, riassunto, pagina di presentazione, file**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Creare una pagina HTML di presentazione per documento con riassunto, link di download e alternativa accessibile. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Realizzabile con `eclair-extension/1` e il contratto di tema: route GET pubbliche memorizzabili in cache, pagine di amministrazione protette, blocchi e impostazioni dichiarativi, task pianificati, asset. Verificare prima che un blocco o un'impostazione nativi non siano sufficienti.
7. **Invariante di sicurezza:** Nessun PDF contenente dati personali viene pubblicato senza consenso. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Verificare link, peso, titolo del documento e pagina di presentazione» e il test di rifiuto «Un PDF rimosso restituisce una risposta pulita e non un link rotto nelle pagine». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Pacchetto `extension.json`/`extension.php` o pacchetto di tema validato, solo se un blocco o un'impostazione nativi non sono sufficienti.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Verificare link, peso, titolo del documento e pagina di presentazione.
- Un PDF rimosso restituisce una risposta pulita e non un link rotto nelle pagine.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `native-v2-workflow`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
