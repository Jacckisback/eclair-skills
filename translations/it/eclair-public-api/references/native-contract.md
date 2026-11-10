# Applicazione del contratto nativo alla skill eclair-public-api

Questa skill utilizza esclusivamente ciò che Éclair CMS 2.0.x fornisce: le funzioni del core, il contratto di tema e il contratto `eclair-extension/1`. Riferimento ufficiale: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posizione di questa skill

La lettura pubblica (GET, memorizzabile in cache) è realizzabile oggi. Qualsiasi scrittura da parte di un visitatore richiede una route POST pubblica che il core 2.0 non apre alle estensioni (PR #19 in bozza, non fusa): non simularla.

## Salvaguardia pratica

Su un vero checkout, rileggere `eclair/index.php`, eseguire `php tools/validate.php` su ogni pacchetto prodotto e `php tests/run.php`. Se la richiesta va oltre le funzioni native, le route GET pubbliche, le pagine di amministrazione protette, i blocchi, le impostazioni e `Store`, produrre una richiesta di evoluzione distinta; **non simularne mai la disponibilità**.
