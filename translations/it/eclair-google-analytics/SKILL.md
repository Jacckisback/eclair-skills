---
name: eclair-google-analytics
description: "Collegare Google Analytics rispettando consenso e politica di sicurezza. Use on Éclair CMS 2.x when the user wants to: collegare Google Analytics rispettando consenso e politica di sicurezza. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Google Analytics — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **collegare Google Analytics rispettando consenso e politica di sicurezza**. Questa funzione è **in parte bloccata dal contratto del core**: la skill consegna ciò che è nativo e documenta lo scostamento. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Site Kit, MonsterInsights. Famiglia: Integrazioni e automazioni.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **ID di misurazione, consenso, eventi**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Verificare prima se basta una misurazione senza cookie; altrimenti consenso preventivo, e presa d'atto che la politica dei contenuti nativa non è aperta alle estensioni. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Una parte dipende da un punto di aggancio assente dal contratto 2.0 (tipi di contenuto, contributo SEO o JSON-LD, politica di contenuto per estensione, filtro di rendering). Consegnare la parte nativa e documentare con precisione lo scostamento, senza aggiramenti.
7. **Invariante di sicurezza:** Nessuno script di misurazione caricato prima del consenso né aggirando la Content-Security-Policy. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Verificare l'assenza di richieste prima del consenso» e il test di rifiuto «Dopo il rifiuto, nessun dato viene inviato». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Pacchetto o impostazioni per la parte nativa, e nota di scostamento precisa per la parte bloccata.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Verificare l'assenza di richieste prima del consenso.
- Dopo il rifiuto, nessun dato viene inviato.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `partly-blocked-by-core-contract`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
