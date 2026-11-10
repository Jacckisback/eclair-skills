---
name: eclair-auth-roles
description: Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles.
---

# Éclair Auth & Roles — distinguere admin e membri

## Realtà v2
`Eclair\Auth` e `Users` controllano **l'amministrazione** con i suoi permessi (`content`, `settings`, `security`, ecc.). Non sono una directory di clienti, studenti o membri, e non devono essere piegati a ruoli `customer/student`.

## Procedura
1. Consultare `Users`, `Auth`, `Admin`, `Security`, `Session`, `RateLimit` e il permesso richiesto da ogni route admin `eclair-extension/1`.
2. Per una funzione di amministrazione, dichiarare `routes.admin[]` con il `right` esatto e affidarsi alla verifica CSRF del core. Verificare l'accesso per ogni ruolo esistente.
3. Per un'area pubblica clienti/studenti: produrre una RFC di identity provider oppure un componente server dedicato e sottoposto ad audit, con storage adeguato; **non** esporre le route sensibili tramite GET pubblico.
4. Definire la sessione membro indipendente, i cookie `Secure/HttpOnly/SameSite`, le autenticazioni progressive, il rate limiting, il recupero e la verifica dell'email.
5. Permessi: identificare sistematicamente il soggetto tramite una sessione server verificata, poi controllare l'oggetto e l'ambito (IDOR/BOLA) a ogni richiesta.
6. Testare l'assenza di privilegi ereditati dall'admin, il cambio di ruolo, la revoca, il reset, le race condition di sessione, gli accessi tra account, CSRF e il rifiuto per impostazione predefinita.

## Dimostratore nativo v1.0
L'estensione `examples/extensions/member-directory/` fornisce un esempio **solo admin** per Éclair 2.0:
- `routes.admin`: GET + POST (`users`) con controlli rafforzati negli handler; `routes.public`: array vuoto.
- `MemberAccounts` e `MemberSessions` restano indipendenti da `Eclair\Users/Auth/Session`; account `pending` obbligatorio al provisioning.
- I dati risiedono esclusivamente sotto `data/ext/member-directory/` tramite `Store`. Mai in `data/users.php`.
- `MemberPermissions::allows` riceve un token di sessione verificato, non un'identità fornita dal chiamante.
- Non è attivata né la registrazione pubblica, né l'invio di email, né il recupero della password, né una gestione reale delle sessioni HTTP.
- L'API POST pubblica richiede una RFC/un nuovo contratto del core e una validazione end-to-end prima del deployment.
Leggere `references/member-directory-v1.md` prima di costruire un LMS, un forum o un e-commerce.

## Deliverable
Matrice di permessi e risorse, modello delle minacce, piano di identità, set di test e indicazione «nativa / RFC richiesta».

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Il prototipo v1.1 dispone di handler pubblici GET modulo + POST accesso/disconnessione + GET area privata. Sono validi solo dopo l'aggiunta approvata del contratto POST. Sessioni dei membri distinte da quelle degli admin, token opaco, CSRF double-submit e CSRF di sessione alla disconnessione; nessun ruolo admin/editor concesso.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
