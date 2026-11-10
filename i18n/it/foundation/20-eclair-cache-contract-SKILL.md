---
name: eclair-cache-contract
description: Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets.
---

# Éclair Cache Contract — mantenere la cache sicura

## Decisione
1. Leggere `eclair/index.php`, `Cache.php`, `Extensions::route()` e `docs/EXTENSION-CONTRACT.md` del core v2 di destinazione.
2. Per le pagine di estensione con contenuto pubblico identico per tutti, `routes.public[].cache` può essere `true` dopo la verifica delle dipendenze di rendering.
3. Per contenuti privati, stati utente, carrelli, token o prezzi personalizzati: **nessuna cache condivisa** (`Cache-Control: private, no-store`), `noindex` pertinente e contratto di autenticazione lato server. Non sostenere mai che un `cache:false` implementi da solo l'autenticazione.
4. Misurare GET/HEAD e query string, prima generazione e poi cache HIT, modifica dei dati, attivazione/disattivazione e migrazioni. Verificare le route del CMS e l'indice `data/ext-public.php`.
5. Non aggiungere mai lookup o letture di registro al percorso rapido `index.php` senza un budget misurato e una giustificazione di sicurezza.
6. Testare `php tools/measure.php --check` e i budget in `tools/budgets.json`, poi confrontare con una baseline pulita con la stessa versione di PHP e gli stessi dati.
7. Verificare la purga dopo l'attivazione e che le pagine pubbliche non interessate restino memorizzabili in cache; testare cookie e header in condizioni di concorrenza.

## Deliverable
Matrice URL × metodo × identità × cache, misure e test di isolamento.

## V1.0 — Identità e cache
Non servire mai una pagina personalizzata a partire da una cache condivisa. Le route di amministrazione esistenti sono già `private, no-store`; le future pagine pubbliche dei membri richiedono un contratto di route privata prima di qualsiasi apertura. Non presumere mai che `cache:false` implementi automaticamente garanzie complete di sessione/CSRF.

## Éclair 2.0 — prototipo v1.1 (sperimentale)
I moduli pubblici GET usano `Security::formField()` e devono essere dichiarati `cache:false`. Le loro risposte non devono raggiungere il fast path del core. POST è escluso dal fast path e forzato a no-store. Testare la purga all'attivazione del modulo e verificare l'assenza di cookie/identità nell'HTML della cache condivisa.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
