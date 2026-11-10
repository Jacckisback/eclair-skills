# Éclair Member Directory — riferimento v1.0

Un dimostratore nativo Éclair 2.0 è fornito in `examples/extensions/member-directory/` alla radice della distribuzione sorgente; non è incluso nella copia autonoma della skill.

- `schema`: `eclair-extension/1`; `requires.eclair`: `>=2.0.0`.
- Route `admin`: GET radice, POST `/create`, POST `/disable`; permesso `users`.
- Nessuna route pubblica. Nessun login pubblico e nessuna email di validazione viene inviata.
- `Store`: chiavi `ext/member-directory/...`, scrittura sotto lock, limite di 1 000 membri a titolo sperimentale.
- Sessione membro distinta dalle sessioni dell'amministrazione, token opaco a 256 bit sottoposto a hash a riposo, revoca tramite epoch.
- Attivazione dopo la prova dell'email: non fornita dalla superficie HTTP. Un ruolo membro non può essere `admin` o `editor`.
- Installazione: copiare l'estensione in `site/extensions/member-directory`, superare `tools/validate.php` del core 2.0, importare e attivare manualmente solo in laboratorio.
- Per account attivi destinati al pubblico: RFC per un POST pubblico sicuro, validazione dell'email, rate limiting, flusso di reset e test nativi. Nessuna route GET deve creare/modificare un account o una sessione.
