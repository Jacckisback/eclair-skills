# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

Il prototipo v1.1 dispone di handler pubblici GET modulo + POST accesso/disconnessione + GET area privata. Sono validi solo dopo l'aggiunta approvata del contratto POST. Sessioni dei membri distinte da quelle degli admin, token opaco, CSRF double-submit e CSRF di sessione alla disconnessione; nessun ruolo admin/editor concesso.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
