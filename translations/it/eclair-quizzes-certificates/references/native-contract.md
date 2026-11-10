# Applicazione del contratto nativo alla skill eclair-quizzes-certificates

Questa skill utilizza esclusivamente ciò che Éclair CMS 2.0.x fornisce: le funzioni del core, il contratto di tema e il contratto `eclair-extension/1`. Riferimento ufficiale: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posizione di questa skill

Le pagine di presentazione dei corsi possono essere pubbliche GET. I corsi a pagamento, i progressi e le valutazioni richiedono un'identità membro qualificata, verifiche di accesso a livello di oggetto e scritture private non memorizzabili in cache.

## Salvaguardia pratica

Su un vero checkout, rileggere `eclair/index.php`, eseguire `php tools/validate.php` su ogni pacchetto prodotto e `php tests/run.php`. Se la richiesta va oltre le funzioni native, le route GET pubbliche, le pagine di amministrazione protette, i blocchi, le impostazioni e `Store`, produrre una richiesta di evoluzione distinta; **non simularne mai la disponibilità**.
