---
name: eclair-extension-builder
description: Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract.
---

# Éclair Extension Builder — costruire un'estensione realmente installabile in v2

## Obiettivo
Creare un **pacchetto `eclair-extension/1` conforme al core v2**. Non usare il manifest `manifest.json` o i file `events.php` / `services.php` dei vecchi prototipi come se fossero supportati.

## Processo
1. Leggere `references/core-map.md`, `docs/EXTENSION-CONTRACT.md`, `docs/schemas/extension.schema.json` e `examples/extensions/bonjour` del checkout.
2. Verificare `ECLAIR_VERSION` e il contratto `eclair-extension/1` tramite il codice e, se accessibile, l'API delle capacità.
3. Definire `id`, `version`, `requires`, `depends`, `provides`, `entry`, route, blocchi, campi, asset, `tasks`, migrazioni; usare unicamente i campi dello schema.
4. Consegnare in `site/extensions/<id>/` **senza scrivere in `app/`**; l'entry PHP deve restituire un oggetto e non deve produrre alcun output al caricamento.
5. Controllare l'output con `e()`; leggere le impostazioni da `$ctx['settings']`; archiviare tramite `Eclair\Store` sotto `$ctx['data']`. Per i segreti: posizione privata e politica di esclusione dai backup documentata.
6. Solo route pubbliche GET. Su una pagina pubblica che mostra un dato di sessione o individuale: fermarsi e richiedere un nuovo contratto di identità/cache; nessun falso aggiramento.
7. Calcolare gli SHA-256 dei file e dichiararli in `files`, eccetto `extension.json`. Generare un pacchetto ZIP la cui radice contiene il manifest.
8. `php tools/validate.php chemin/extension --json`; correggere tutti gli errori prima di proporre l'importazione, poi testare `php tests/run.php` e `php tools/measure.php --check`.
9. Una persona autorizzata importa, visualizza in anteprima/controlla, attiva; documentare la disattivazione, la rimozione del codice e la conservazione dei dati.

## Deliverable
`extension.json`, entry `extension.php`, riferimenti, test, prova di validazione ufficiale e manuale di installazione. Esempio originale in `examples/extensions/skill-sample/`; verificare sul core esatto prima del deployment.

## V1.0 — Modello avanzato fornito
Consultare `examples/extensions/member-directory`: dimostra route admin GET/POST native e una libreria PHP caricata soltanto dall'estensione. Non trasformare il suo GET admin in un accesso pubblico né aggiungere un POST a `routes.public` (contratto v2 incompatibile).

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Un prototipo di route POST pubblica si trova in `examples/extensions/member-directory/`. Viene rifiutato dal core 2.0 ufficiale. Usare il manifest solo con la patch sperimentale e l'accordo esplicito di un maintainer, mai in produzione. POST richiede `cache:false`, TLS, CSRF, reindirizzamento relativo.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
