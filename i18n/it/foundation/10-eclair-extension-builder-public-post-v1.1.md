# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

Un prototipo di route POST pubblica si trova in `examples/extensions/member-directory/`. Viene rifiutato dal core 2.0 ufficiale. Usare il manifest solo con la patch sperimentale e l'accordo esplicito di un maintainer, mai in produzione. POST richiede `cache:false`, TLS, CSRF, reindirizzamento relativo.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
