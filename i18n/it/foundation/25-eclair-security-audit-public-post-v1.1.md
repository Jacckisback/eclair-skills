# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

Il prototipo v1.1 prevede una limitazione `RateLimit::attempt` prima dell'hash, una separazione rigorosa membri/admin e token di sessione a 256 bit. Valutare la sicurezza degli `Origin`, di TLS dietro reverse proxy, CSRF, IDOR, enumerazione degli account, fughe di informazioni e concorrenza. Non confondere test isolati e audit in produzione.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
