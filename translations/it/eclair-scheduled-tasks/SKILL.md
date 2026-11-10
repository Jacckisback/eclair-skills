---
name: eclair-scheduled-tasks
description: "Automatizzare elaborazioni periodiche con i task di estensione. Use on Éclair CMS 2.x when the user wants to: automatizzare elaborazioni periodiche tramite i task di estensione. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Task pianificati — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **automatizzare elaborazioni periodiche tramite i task di estensione**. Questa funzione è **realizzabile oggi** con il contratto nativo (tema, blocchi, route GET, pagine di amministrazione, task). Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** WP-Cron, WP Crontrol. Famiglia: Amministrazione e manutenzione.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Task, frequenza, ultima esecuzione, risultato**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Dichiarare il task nel manifest (al massimo una volta all'ora), chiamare l'indirizzo segreto del core dallo scheduler del provider di hosting, registrare nei log. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Realizzabile con `eclair-extension/1` e il contratto di tema: route GET pubbliche memorizzabili in cache, pagine di amministrazione protette, blocchi e impostazioni dichiarativi, task pianificati, asset. Verificare prima che un blocco o un'impostazione nativi non siano sufficienti.
7. **Invariante di sicurezza:** L'indirizzo segreto dei task non viene mai pubblicato; ogni task è idempotente. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Eseguire il task due volte di seguito e verificare un solo effetto» e il test di rifiuto «Una chiamata senza il token segreto non attiva nulla». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Pacchetto `extension.json`/`extension.php` o pacchetto di tema validato, solo se un blocco o un'impostazione nativi non sono sufficienti.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Eseguire il task due volte di seguito e verificare un solo effetto.
- Una chiamata senza il token segreto non attiva nulla.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `native-v2-workflow`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
