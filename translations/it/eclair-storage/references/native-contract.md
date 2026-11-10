# Applicazione del contratto nativo alla skill eclair-storage

Questa skill utilizza esclusivamente il contratto `eclair-extension/1` fornito in Éclair CMS 2.0.0 e non le API dei vecchi prototipi. Riferimento ufficiale: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Salvaguardia pratica

Su un vero checkout, rileggere `eclair/index.php`, eseguire `php tools/validate.php` su ogni pacchetto prodotto e `php tests/run.php`. Se il contratto richiesto va oltre le route GET pubbliche, i permessi admin, i campi/blocchi e `Store`, produrre una RFC distinta; **non simularne mai la disponibilità**.
