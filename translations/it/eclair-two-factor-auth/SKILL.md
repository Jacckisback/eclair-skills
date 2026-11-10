---
name: eclair-two-factor-auth
description: "Attivare l'autenticazione a due fattori nativa per tutto il team. Use on Éclair CMS 2.x when the user wants to: attivare l'autenticazione a due fattori nativa per tutto il team. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Autenticazione a due fattori — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **attivare l'autenticazione a due fattori nativa per tutto il team**. Questa funzione è **già integrata nel core di Éclair 2.0**: la skill ne guida la configurazione e la verifica, senza scrivere alcuna estensione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Two Factor, WP 2FA. Famiglia: Sicurezza e privacy.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Account, segreto TOTP, codici di emergenza**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Far attivare l'autenticazione a due fattori da ogni persona, riporre i codici di emergenza, prevedere la perdita del dispositivo. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** La funzione esiste nel core: configurarla tramite l'amministrazione oppure, in bozza, tramite il connettore MCP. Non duplicarla in un'estensione e non modificare mai il core per adattarla; se un'esigenza va oltre ciò che il core offre, segnalarla come scostamento.
7. **Invariante di sicurezza:** I segreti e i codici di emergenza non vengono mai copiati in una chat, in un'e-mail o in un repository. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Attivare, disconnettersi, riconnettersi con il secondo fattore» e il test di rifiuto «Una password corretta senza secondo fattore non dà accesso». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Impostazioni e contenuti preparati tramite l'amministrazione o in bozza tramite il MCP; **nessuna estensione** finché il nativo è sufficiente.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Attivare, disconnettersi, riconnettersi con il secondo fattore.
- Una password corretta senza secondo fattore non dà accesso.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `core-builtin-configuration-workflow`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
