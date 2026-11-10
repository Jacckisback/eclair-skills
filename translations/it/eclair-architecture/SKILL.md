---
name: eclair-architecture
description: Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC.
---

# Éclair Architecture — preservare il core v2

## Obiettivo
Progettare la soluzione richiesta **senza ricopiare un sistema di estensioni** e senza sovraccaricare la route di cache. Iniziare da `references/core-map.md` e dal codice del checkout corrente.

## Svolgimento operativo
1. Rilevare il commit, la versione `ECLAIR_VERSION`, PHP e le capacità disponibili tramite `/admin/api/capabilities` se l'accesso è autorizzato.
2. Classificare l'obiettivo: contenuto/impostazione nativi, tema del sito, estensione `eclair-extension/1`, servizio esterno, oppure lacuna del contratto pubblico che richiede una RFC.
3. Cercare prima `Extensions`, `Themes`, `Packages`, `Migrations`, `Store`, `Cache`, `Site`, `Seo`, `Security`, `Mcp` e i documenti `docs/ARCHITECTURE-2.md`/`docs/STATUS-2.md`.
4. Descrivere i confini: codice sotto `site/extensions/` o `site/themes/`, dati tramite `Store` e `$ctx['data']`, media sotto `media/`, nessuna sostituzione di `app/`.
5. Distinguere rigorosamente il contratto nativo (`eclair-extension/1`) dalle vecchie sperimentazioni v0.8 (route/permessi/SQL/outbox), incompatibili con v2 senza porting.
6. Produrre una decisione di architettura esplicita: alternative, limiti dell'API, rischi, rollback, test di compatibilità e indicatori di prestazioni.
7. Far rileggere e poi validare con `php tests/run.php`, `php tools/measure.php --check` e i test pertinenti di `tests/extensions.php`.

## Non negoziabili
Preservare SEO/GEO, markup canonico, protezioni CSRF/CSP, gestione dell'autenticazione e cache calda. Un'estensione non si attiva mai da sola. Non dichiarare di gestire né un checkout transazionale, né gli account degli studenti, finché questi contratti non sono implementati e testati.

## Deliverable
ADR e mappatura prima/dopo, decisione «nativa / estensione / core RFC», vincoli, test e piano di rollback. Il modello `assets/architecture-decision.md` può servire da punto di partenza.

## V1.0 — Estensioni per i membri
L'estensione nativa `examples/extensions/member-directory` illustra gli account pubblici separati: nessun nuovo ruolo in `Eclair\Users`. Un core 2.0 riceve le estensioni tramite `site/extensions/<id>`; nessuna scrittura in `app/`.

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Éclair 2.0.0 dispone ora di un contratto sperimentale di POST pubblico unicamente se la patch v1.1 è applicata su un branch di sviluppo. Il core ufficiale **non** fornisce questo contratto. Nessuna modifica diretta del core da una skill; preparazione di una RFC e test preliminari.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
