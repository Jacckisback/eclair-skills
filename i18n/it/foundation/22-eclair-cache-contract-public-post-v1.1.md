# Route HTTP pubbliche per i membri — Éclair 2.0.0 sperimentale

I moduli pubblici GET usano `Security::formField()` e devono essere dichiarati `cache:false`. Le loro risposte non devono raggiungere il fast path del core. POST è escluso dal fast path e forzato a no-store. Testare la purga all'attivazione del modulo e verificare l'assenza di cookie/identità nell'HTML della cache condivisa.

La patch sorgente si trova in `core-patch/` della distribuzione completa, non inclusa in una copia autonoma della skill. Non considerare mai questa patch come un'API ufficiale prima della sua fusione upstream.
