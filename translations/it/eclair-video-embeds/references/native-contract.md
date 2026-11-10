# Applicazione del contratto nativo alla skill eclair-video-embeds

Questa skill utilizza esclusivamente ciò che Éclair CMS 2.0.x fornisce: le funzioni del core, il contratto di tema e il contratto `eclair-extension/1`. Riferimento ufficiale: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posizione di questa skill

La funzione esiste nel core: configurarla tramite l'amministrazione oppure, in bozza, tramite il connettore MCP. Non duplicarla in un'estensione e non modificare mai il core per adattarla; se un'esigenza va oltre ciò che il core offre, segnalarla come scostamento.

## Salvaguardia pratica

Su un vero checkout, rileggere `eclair/index.php`, eseguire `php tools/validate.php` su ogni pacchetto prodotto e `php tests/run.php`. Se la richiesta va oltre le funzioni native, le route GET pubbliche, le pagine di amministrazione protette, i blocchi, le impostazioni e `Store`, produrre una richiesta di evoluzione distinta; **non simularne mai la disponibilità**.
