---
name: eclair-test-suite
description: Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations.
---

# Éclair Test Suite — una prova prima della pubblicazione

## Ordine di verifica
1. Rilevare il commit e `ECLAIR_VERSION`; esigere il contratto v2 ufficiale. Senza un checkout completo, limitare le affermazioni ai test realmente eseguibili.
2. `php -l` di ogni file PHP prodotto, poi `php tools/validate.php site/extensions/<id> --json` con il core corrispondente.
3. `php tests/run.php --unit`, poi `php tests/run.php` (HTTP, auth, route, cache, backup, estensioni, temi, migrazione WordPress).
4. `php tools/measure.php --check`; confrontare la cache calda e il budget di memoria/tempo con il core non modificato.
5. Testare installazione inattiva, attivazione, migrazione idempotente, update, conflitto di route, disattivazione, conservazione dei dati, rimozione del codice ed eventuale purga manuale.
6. In caso di account membri/SQL: esigere test PHP/PDO reali, multi-processo, autorizzazioni per oggetto, webhook firmati e ripristino da backup. `pdo_sqlite` assente = test bloccato, non superato.
7. CI raccomandata: matrice PHP da 8.1 a 8.5, `tests.yml` ufficiale, archivio costruito e server Apache/Nginx; aggiungere job specifici per la funzionalità.
8. Produrre una tabella test eseguiti / falliti / bloccati. Non riportare mai «compatibile con la produzione» a partire da una fixture isolata.

## Deliverable
Script e fixture, rapporto di esecuzione, copertura dei casi avversi, budget e strategia di rollback.

## V1.0 — Verifiche supplementari
Eseguire `php tests/member-directory.php`, `python3 -m unittest discover -s tests -v` e `python3 scripts/verify_sample.py`. Su un checkout Éclair 2.0 completo, eseguire **tassativamente** `php tools/validate.php examples/extensions/member-directory --json`, poi i test PHP/HTTP del CMS completo e il budget `tools/measure.php --check` prima di qualsiasi proposta di fusione.

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Testare `php tests/member-directory.php` + `php tests/member-public.php` e i test Python. Su un vero clone di Éclair 2.0.0, applicare la patch a una feature branch pulita, eseguire `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` e prove HTTP/TLS. Nessuna fusione senza questi criteri.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
