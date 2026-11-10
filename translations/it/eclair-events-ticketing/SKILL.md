---
name: eclair-events-ticketing
description: "Vendere posti, biglietti e ingressi per eventi. Use on Éclair CMS 2.x when the user wants to: commercializzare posti, biglietti e ingressi. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Eventi e biglietti — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **commercializzare posti, biglietti e ingressi**. Questa funzione **richiede capacità assenti dal core 2.0**: la skill consegna progettazione, mockup sicuro e test, non una messa in produzione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** The Events Calendar, Event Tickets. Famiglia: App di business.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Evento, sessione, tipo di posto, prenotazione, biglietto, scansione, rimborso**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Separare le quote per sessione; emettere biglietti univoci dopo il pagamento confermato; gestire controllo d'ingresso atomico e trasferimento. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** Le vetrine pubbliche sono possibili con GET; prenotazioni, pagamenti, candidature, CRM e dati personali richiedono POST sicuro, uno storage adeguato e permessi verificati lato server.
7. **Invariante di sicurezza:** Il codice QR non contiene dati personali in chiaro e non autorizza più ingressi. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Testare doppia scansione, annullamento e ultimo biglietto simultaneo» e il test di rifiuto «Stesso biglietto presentato a due ingressi => una sola ammissione accettata». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Dossier di progettazione, mockup GET sicuro se utile, test bloccanti e richiesta di evoluzione del core; **nessun pacchetto di produzione**.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Testare doppia scansione, annullamento e ultimo biglietto simultaneo.
- Stesso biglietto presentato a due ingressi => una sola ammissione accettata.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `design-workflow-requires-verified-core-capabilities`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
