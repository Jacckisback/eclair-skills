---
name: eclair-theme-builder
description: "Produrre un tema Éclair v2 compatibile con gli aggiornamenti. Use on Éclair CMS 2.x when the user wants to: produrre un tema Éclair v2 compatibile con gli aggiornamenti. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Creazione di temi — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **produrre un tema Éclair v2 compatibile con gli aggiornamenti**. Questa funzione è **realizzabile oggi** con il contratto nativo (tema, blocchi, route GET, pagine di amministrazione, task). Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Temi child e temi a blocchi. Famiglia: Design e UX.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **theme.json, stili, asset, template dichiarati, licenza e provenienza**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Partire dal tema di esempio ufficiale, impiegare variabili e template supportati, testare la preview e poi lo ZIP, verificare la compatibilità di versione. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Éclair v2 espone temi sotto site/themes e blocchi dichiarativi di estensione. Non modificare né app/, né index.php, né la CSP, né la generazione della cache; validare i temi tramite tools/validate.php.
7. **Invariante di sicurezza:** Non rifare mai SEO head e canonical né toccare i file del core. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Testare validatore del tema, attivazione, anteprima e ripristino» e il test di rifiuto «Un template difettoso non rende il sito inaccessibile grazie al ripiego previsto». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Pacchetto `extension.json`/`extension.php` o pacchetto di tema validato, solo se un blocco o un'impostazione nativi non sono sufficienti.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Testare validatore del tema, attivazione, anteprima e ripristino.
- Un template difettoso non rende il sito inaccessibile grazie al ripiego previsto.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `native-v2-workflow`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
