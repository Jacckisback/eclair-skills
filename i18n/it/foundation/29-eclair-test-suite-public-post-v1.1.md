# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

Testare `php tests/member-directory.php` + `php tests/member-public.php` e i test Python. Su un vero clone di Éclair 2.0.0, applicare la patch a una feature branch pulita, eseguire `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` e prove HTTP/TLS. Nessuna fusione senza questi criteri.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
