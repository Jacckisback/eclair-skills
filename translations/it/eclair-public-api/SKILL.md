---
name: eclair-public-api
description: "Esporre dati pubblici del sito in JSON. Use on Éclair CMS 2.x when the user wants to: esporre dati pubblici del sito in JSON. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# API pubblica in lettura — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **esporre dati pubblici del sito in JSON**. La **parte pubblica in lettura è realizzabile oggi**; le scritture da parte dei visitatori richiedono più di quanto offra il contratto attuale. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** API REST di WordPress. Famiglia: Sviluppo e strumenti.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Risorsa, campi pubblici, paginazione, versione**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Dichiarare route GET memorizzabili in cache che restituiscono JSON limitato e versionato; documentare che la scrittura non è aperta. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** La lettura pubblica (GET, memorizzabile in cache) è realizzabile oggi. Qualsiasi scrittura da parte di un visitatore richiede una route POST pubblica che il core 2.0 non apre alle estensioni (PR #19 in bozza, non fusa): non simularla.
7. **Invariante di sicurezza:** Vengono esposti soltanto contenuti già pubblici; nessun identificativo interno sensibile. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Leggere elenco e dettaglio, paginazione e caso vuoto» e il test di rifiuto «Un contenuto non pubblicato non viene restituito da alcuna route». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Pacchetto in sola lettura (route GET) validato, e piano scritto per la parte in scrittura, chiaramente contrassegnata come non consegnata.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Leggere elenco e dettaglio, paginazione e caso vuoto.
- Un contenuto non pubblicato non viene restituito da alcuna route.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `public-read-only-prototype-possible`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
