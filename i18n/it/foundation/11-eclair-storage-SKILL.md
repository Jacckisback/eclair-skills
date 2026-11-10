---
name: eclair-storage
description: Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress.
---

# Éclair Storage — scegliere la persistenza giusta

## Decisione di storage
1. Per contenuti e impostazioni Éclair, usare `Eclair\Store` e il prefisso `data/ext/<id>/` ottenuto tramite `$ctx['data']`.
2. Verificare `Store::locked`, le scritture atomiche e i volumi realmente gestiti; non inventare garanzie transazionali multi-file.
3. Per ordini/pagamenti/scorte e progressione LMS concorrente: specificare SQLite o MySQL **come dipendenza opzionale del modulo** con le relative migrazioni, vincoli, transazioni, backup e ripresa. Il contratto nativo v2 non fornisce un PDO generico per le estensioni.
4. Dichiarare dati personali, conservazione, cancellazione ed esportazione; non conservare chiavi né token nei backup.
5. Migrazioni native di estensione tramite il manifest `migrations[]` e il metodo `migrate`: additive, versionate, idempotenti. Una migrazione di schema SQL deve avere un piano separato, non essere innescata su una pagina GET.
6. Prevedere un backup coerente, un ripristino a freddo e un test di rollback. Se SQL non è disponibile su hosting condiviso, dichiarare la funzionalità non disponibile anziché ripiegare su una persistenza non affidabile.
7. Testare collisioni, riavvii, concorrenza, duplicati, corruzione, chmod/symlink, backup e riconciliazione.

## Regole
Lo storage nativo senza database deve restare possibile per un sito semplice. I prototipi SQL v0.5/v0.8 non sono installati né riconosciuti da v2. Non promettere l'exactly-once per gli effetti esterni.

## Deliverable
Schema, matrice degli invarianti, protocollo di migrazione/restore, requisiti di hosting, test di transazione e di integrità.

## V1.0 — Modello di account leggeri
Il prototipo `member-directory` rispetta `data/ext/<id>/`, scritture atomiche e un lock globale. Lo storage su più file **non è una transazione SQL**. La quota di 1 000 account è un limite di laboratorio: qualsiasi progetto commerciale con molti membri deve prima disporre del contratto SQL transazionale.

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Lo storage del dimostratore utilizza ancora i file protetti di `Store` e un lock globale. È limitato a 1000 account; nessuna promessa di atomicità multi-file, di accesso su larga scala o di tolleranza ai guasti transazionali. Un backend SQL è un prerequisito prima dell'esercizio in ambito business.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
