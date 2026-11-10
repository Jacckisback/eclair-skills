---
name: eclair-crm-integration
description: "Sincronizzare lead e clienti con un CRM, senza duplicati. Use on Éclair CMS 2.x when the user wants to: collegare potenziali clienti/clienti a un CRM senza duplicati. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Sincronizzazione CRM — Éclair CMS 2.x

## Attivazione e risultato atteso
Usare questa skill per **collegare potenziali clienti/clienti a un CRM senza duplicati**. Questa funzione **richiede capacità assenti dal core 2.0**: la skill consegna progettazione, mockup sicuro e test, non una messa in produzione. Questa skill è un **workflow per agenti**, non un'estensione PHP funzionante né una garanzia di conformità.

**Equivalente WordPress:** Plugin HubSpot o Salesforce. Famiglia: Integrazioni e automazioni.

## Diagnosi obbligatoria prima di ogni modifica
1. Leggere `references/core-map.md` (ciò che il core fa già) e `references/native-contract.md`; verificare la versione reale del CMS e le capacità in `GET /<admin>/api/capabilities` (se l'accesso è autorizzato).
2. Leggere `references/family-contract.md` e `references/acceptance.md`. Non copiare mai in Éclair 2 il vecchio sistema di pack v0.x né codice PHP di WordPress.
3. Identificare il modello di dati: **Contatto, azienda, consenso, mapping, chiave esterna, provenienza**. Documentare ciò che è pubblico, ciò che è privato e da dove proviene ogni dato.

## Procedura specifica
4. **Percorso:** Mappare campi rigorosi, differenziare aggiornamenti direzionali e fusione, fornire riconciliazione ed esportazione/eliminazione. Descrivere gli stati e gli errori prima di scrivere codice.
5. **Posizioni:** codice specifico del sito in `site/extensions/<id>/`, aspetto in `site/themes/<id>/`, dati sotto `$ctx['data']`, contenuti e impostazioni tramite l'amministrazione o il MCP. Non modificare mai `app/`, `assets/`, `index.php` né l'updater.
6. **Contratto attuale:** I task nativi esistono (minimo 3 600 secondi). I webhook in ingresso e le interazioni dei membri richiedono route POST qualificate, una validazione della firma e, per gli effetti di business, una outbox idempotente.
7. **Invariante di sicurezza:** Non esportare contatti senza base giuridica né scope minimi. Verificare anche i permessi lato server, l'escape con `e()`, la validazione dei dati e l'assenza di segreti o dati personali nell'HTML pubblico o in una cache condivisa.
8. **Prove:** scrivere il test positivo «Testare fusione, email modificata, conflitto, eliminazione e ripresa» e il test di rifiuto «Lo stesso contatto risincronizzato non crea più duplicati nel CRM». Misurare le regressioni di SEO e di prestazioni, documentare il rollback.
9. **Validazione nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` su un checkout ufficiale per ogni pacchetto prodotto. Per una parte non supportata dal core, fornire una nota di scostamento e un test bloccante, mai un successo fittizio.

## Deliverable obbligatori
- Mini-specifica: obiettivo, utenti, percorsi, stati, dati, misure.
- Matrice di autorizzazioni e di cache: route, metodo, sessione, visibilità, indicizzazione.
- Dossier di progettazione, mockup GET sicuro se utile, test bloccanti e richiesta di evoluzione del core; **nessun pacchetto di produzione**.
- Test dei casi positivi e dei rifiuti, procedura di disattivazione che conserva i dati, nota di compatibilità.

## Criteri di accettazione
- Testare fusione, email modificata, conflitto, eliminazione e ripresa.
- Lo stesso contatto risincronizzato non crea più duplicati nel CRM.
- Nulla viene pubblicato, attivato o messo in produzione senza una persona autorizzata; non si promette alcun punteggio, posizionamento o citazione da parte di un'IA.
- Le parti non supportate da Éclair 2.0 sono segnalate esplicitamente come **non consegnabili in produzione**.

**Stato di maturità di questa skill:** `design-workflow-requires-verified-core-capabilities`. Vedere `references/acceptance.md` per i casi di prova riproducibili.
