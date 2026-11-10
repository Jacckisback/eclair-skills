---
name: eclair-security-audit
description: Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security.
---

# Éclair Security Audit — revisione prima dell'attivazione

## Perimetro
1. Stabilire la versione del core, la provenienza dell'estensione, i file eseguibili e i permessi richiesti.
2. Esigere un contratto `extension.json` conforme e impronte SHA-256 per i file; verificare symlink, path traversal, script imprevisti, ZIP bomb, dimensioni, metodi e route riservate.
3. Controllare separatamente il `right` nativo della route admin e le autorizzazioni di business sugli oggetti; un permesso `content` non autorizza a leggere l'ordine di un altro cliente.
4. Testare CSRF, rate limiting, session fixation, accesso diretto ai file, XSS nell'HTML restituito, SQL injection, SSRF degli URL esterni e gestione dei segreti.
5. Pagine pubbliche con `cache:true`: assenza di dati personali e di varianti per utente. Pagine admin: header, autenticazione e rifiuto per impostazione predefinita.
6. Per un checkout: webhook firmato con verifica lato server, idempotenza, importi, valuta, IVA e transizioni di stato transazionali prima della consegna.
7. Per eventi di business: ricordare che v2 non integra un bus/outbox standard; progetto separato con test di guasto e nessuna promessa di exactly-once per gli effetti remoti.
8. Non eseguire mai moduli non sottoposti ad audit con la fiducia del processo PHP.

## Prove minime
`php tools/validate.php chemin/extension --json`, `php tests/run.php`, `php tools/measure.php --check` e scenari negativi HTTP su un'installazione di test. Nessun rapporto di sicurezza è una certificazione automatica.

## Deliverable
Elenco dei rischi classificati, dimostrazioni riproducibili, correzioni, limiti residui e decisione esplicita Go/No-Go.

## V1.0 — Test dell'identità
Sottoporre ad audit il prototipo `member-directory`: nessun account membro in `data/users.php`, password mai restituita, stato `pending` per impostazione predefinita, ruoli `admin/editor` vietati, epoch di revoca, controllo dell'oggetto proprio/altrui, cookie `__Host-` HTTPS. I test locali non equivalgono a un audit in produzione.

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Il prototipo v1.1 prevede una limitazione `RateLimit::attempt` prima dell'hash, una separazione rigorosa membri/admin e token di sessione a 256 bit. Valutare la sicurezza degli `Origin`, di TLS dietro reverse proxy, CSRF, IDOR, enumerazione degli account, fughe di informazioni e concorrenza. Non confondere test isolati e audit in produzione.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
