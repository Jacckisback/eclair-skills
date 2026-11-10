# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

Lo storage del dimostratore utilizza ancora i file protetti di `Store` e un lock globale. È limitato a 1000 account; nessuna promessa di atomicità multi-file, di accesso su larga scala o di tolleranza ai guasti transazionali. Un backend SQL è un prerequisito prima dell'esercizio in ambito business.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
