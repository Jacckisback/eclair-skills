---
name: eclair-tags-taxonomies
description: "Riprendere tag o tassonomie personalizzate quando il core offre solo categorie. Use on Éclair CMS 2.x when the user wants to: riprendere tag o tassonomie personalizzate quando il core offre soltanto categorie. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Tag e tassonomie — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **riprendere tag o tassonomie personalizzate quando il core offre soltanto categorie**. Questa funzione è **in parte bloccata dal contratto del core**: la skill consegna ciò che è nativo e documenta lo scostamento. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Tag e tassonomie personalizzate di WordPress. Famiglia: Contenuti e redazione.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Termine, tipo di tassonomia, contenuti collegati, indirizzo di archivio**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Inventariare le tassonomie esistenti, unire quelle che duplicano le categorie, proporre pagine di raggruppamento in GET per il resto e reindirizzare i vecchi archivi. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Una parte dipende da un punto di aggancio assente dal contratto 2.0 (tipi di contenuto, contributo SEO o JSON-LD, politica di contenuto per estensione, filtro di rendering). Consegnare la parte nativa e documentare con precisione lo scostamento, senza aggiramenti.
7. **Invariante di sicurezza:** Non generare centinaia di archivi poveri indicizzabili. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Convertire un insieme di tag in categorie o in pagine di raggruppamento e verificare i reindirizzamenti» e il test di rifiuto «Un vecchio archivio di tag eliminato reindirizza alla pagina più vicina, senza catena». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Pacchetto o impostazioni per la parte nativa, e nota di scostamento precisa per la parte bloccata.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Convertire un insieme di tag in categorie o in pagine di raggruppamento e verificare i reindirizzamenti.
- Un vecchio archivio di tag eliminato reindirizza alla pagina più vicina, senza catena.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `partly-blocked-by-core-contract`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
