# Éclair CMS 2.0.x — mappa del core verificata

Riferimento: repository pubblico `Jacckisback/eclair-cms`, branch `main` verificato il 9 novembre 2026, commit di riferimento `6567d7642ea2227a598c4988e970d43e2e5e0e4f`. **Un agente deve sempre riverificare il checkout reale e `GET /<admin>/api/capabilities`**: questa nota è un'istantanea, non una garanzia di compatibilità futura.

## 1. Già integrato nel core: configurare, non ricostruire

Prima di scrivere una qualsiasi estensione, verificare se l'esigenza è coperta nativamente:

- **Contenuti**: pagine e articoli a blocchi, categorie, menu, autori, bozze, calendario editoriale; blocchi `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Media**: immagini ridimensionate, ricodificate e convertite in WebP responsive, dimensioni esplicite, caricamento differito.
- **Modulo di contatto** e casella di ricezione dei messaggi (permesso `messages`).
- **SEO e GEO**: titoli e descrizioni con analisi in tempo reale, JSON-LD (organizzazione o attività locale, articolo, FAQ, breadcrumb), sitemap con immagini e `hreflang`, feed RSS, Open Graph con immagine di condivisione, reindirizzamenti 301 e gestore dei reindirizzamenti, IndexNow, `llms.txt`, versione Markdown di ogni pagina, politica per i robot di IA.
- **Velocità**: cache statica di ogni pagina pubblica, CSS integrato, un solo script pubblico, nessun cookie pubblico.
- **Sicurezza**: autenticazione a due fattori, limiti ai tentativi, Content-Security-Policy rigorosa, contenuti sanificati, controllo di integrità, registro, aggiornamenti firmati con rollback.
- **Backup**: download e invio pianificato verso uno storage remoto, ripristino.
- **Negozio leggero**: schede prodotto, varianti, categorie, link di pagamento di un fornitore, feed commerciale; **niente carrello, ordini né account cliente**.
- **Funzioni fornite**: affiliazione, pubblicità, calendario, importazione WordPress, recupero di un vecchio sito, monitoraggio dei robot di IA.
- **Assistente IA e connettore MCP**: solo bozze e proposte, mai pubblicazione né eliminazione.
- **Aspetto**: temi e direzioni artistiche, anteprima prima del salvataggio.

## 2. Dove una skill può scrivere

- Codice del core: `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **non modificare mai** per consegnare una funzionalità del sito.
- Estensioni del sito: `site/extensions/<id>/` con `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Temi del sito: `site/themes/<id>/` con `theme.json`.
- Dati di un'estensione: `Eclair\Store`, prefisso `$ctx['data']` (`data/ext/<id>/`), segreti in `data/ext/<id>/secrets.php`.
- Contenuti e impostazioni: esclusivamente tramite l'amministrazione o il connettore MCP.

## 3. Contratto `eclair-extension/1`

- Route pubbliche di un'estensione: **solo GET**, dichiarate nel manifest, memorizzabili in cache oppure no.
- Amministrazione: GET/POST sotto `/<admin>/x/<id>/...`, permessi del core (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) e protezione CSRF.
- Blocchi e impostazioni dichiarativi validati dal core; task pianificati (al massimo una volta all'ora); migrazioni idempotenti; asset pubblicati.
- Il codice di un'estensione è **considerato attendibile, senza sandbox**: l'importazione e l'attivazione richiedono una persona autorizzata.
- Validazione: `php tools/validate.php <dossier> --json`, poi `php tests/run.php` e `php tools/measure.php --check` in un checkout del core.

## 4. Limiti noti della 2.0

- Nessuna route POST pubblica per le estensioni (PR #19 in bozza, non fusa), quindi nessuna iscrizione, commento, ordine o caricamento da parte di un visitatore al di fuori del modulo di contatto nativo.
- Nessuna identità pubblica (cliente, studente, membro) nel contratto nativo.
- Nessun tipo di contenuto specifico di un'estensione; nessun contributo SEO o JSON-LD per estensione; nessuna politica di contenuto (CSP) per estensione; nessun filtro generale di rendering.
- Tag, commenti e tipi di contenuto personalizzati di WordPress non vengono ripresi dall'importazione.
- I vecchi prototipi Éclair Devkit v0.x erano destinati al core 1.14 e **non si applicano** alla 2.0.

Fonti ufficiali:
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
