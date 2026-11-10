# Applicazione del contratto nativo alla skill eclair-product-variants

Questa skill utilizza esclusivamente ciò che Éclair CMS 2.0.x fornisce: le funzioni del core, il contratto di tema e il contratto `eclair-extension/1`. Riferimento ufficiale: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posizione di questa skill

Il core fornisce già un negozio leggero (schede prodotto, varianti, categorie, link di pagamento di un fornitore, feed commerciale): usarlo per primo, senza duplicarlo. Oltre a questo, carrello, ordini e pagamenti hanno bisogno di POST pubblici, di uno storage transazionale affidabile, di webhook autenticati e di idempotenza; Éclair 2.0 ufficiale non fornisce tutto questo. La PR #19 è ancora una bozza: non usare mai una route POST non fusa come prova di compatibilità.

## Salvaguardia pratica

Su un vero checkout, rileggere `eclair/index.php`, eseguire `php tools/validate.php` su ogni pacchetto prodotto e `php tests/run.php`. Se la richiesta va oltre le funzioni native, le route GET pubbliche, le pagine di amministrazione protette, i blocchi, le impostazioni e `Store`, produrre una richiesta di evoluzione distinta; **non simularne mai la disponibilità**.
