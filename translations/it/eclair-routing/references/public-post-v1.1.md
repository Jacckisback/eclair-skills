# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

Le route pubbliche POST **non** sono presenti in Éclair 2.0 ufficiale. La patch proposta v1.1 introduce un'eccezione controllata: metodo POST esplicito, `cache:false`, HTTPS, `Security::checkFormToken()`, risposta `private,no-store`, reindirizzamento 303 relativo. Eseguire sempre prove HTTP con il CMS completo prima della fusione.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
