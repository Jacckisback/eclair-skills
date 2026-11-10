---
name: eclair-routing
description: Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility.
---

# Éclair Routing — proteggere gli URL e la compatibilità

## Procedura
1. Rilevare le route e gli alias esistenti, `Site.php`, `App.php`, `Aliases.php`, `Redirects.php`, `Content::byRoute` e gli URL riservati.
2. Le route pubbliche di estensione `routes.public[]` sono **solo GET** ed elencate esplicitamente. Nessuna route generica `/{slug}` tramite un manifest inventato.
3. Le route admin usano `routes.admin[]`, metodo GET/POST, sotto `/<admin>/x/<id>/...` e con il permesso `right` nativo.
4. Testare prima dell'attivazione le collisioni con articoli/pagine/prodotti, route riservate, slug multilingue, sito in sottocartella e altre estensioni.
5. Preservare il percorso esatto di una migrazione WordPress (slash finale, .html, accenti) tramite i meccanismi v2 `route`/`Aliases`, senza creare più canonical né catene di 301.
6. Per una funzione che richiede route pubbliche POST (checkout, API cliente), documentare una RFC/nuova interfaccia sicura invece di intercettare il core o di aggirare il router.
7. Verificare canonical, sitemap, JSON-LD, noindex per le interfacce private, `HEAD`, risposte 404/405 e cache.

## Deliverable
Tabella delle route, proprietario del namespace, piano dei reindirizzamenti, conflitti rilevati e test HTTP.

## V1.0 — Route pubblica di accesso vietata
I GET pubblici dichiarativi di Éclair 2.0 sono adatti a pagine pubbliche, **non** a un modulo POST di accesso. Nessuna route `/login` né `/register` con effetti collaterali deve essere creata con GET. `member-directory` dichiara soltanto route admin con permesso `users`.

## Éclair 2.0 — prototipo v1.1 (sperimentale)
Le route pubbliche POST **non** sono presenti in Éclair 2.0 ufficiale. La patch proposta v1.1 introduce un'eccezione controllata: metodo POST esplicito, `cache:false`, HTTPS, `Security::checkFormToken()`, risposta `private,no-store`, reindirizzamento 303 relativo. Eseguire sempre prove HTTP con il CMS completo prima della fusione.

## Éclair 2.0 — registrazione e recupero (v1.2 sperimentale)

Leggere `references/member-email-v1.2.md` prima di qualsiasi richiesta di creazione di account clienti/studenti o di recupero della password. Il modulo `member-directory` v0.3 utilizza route pubbliche POST **fuori dal contratto ufficiale**; non promettere mai un'installazione diretta su Éclair 2.0 non modificato né attivare i flussi email senza un URL HTTPS verificato e test nativi. Preferire il sistema di estensioni v2 a qualsiasi modifica della vecchia architettura v0.x. Mantenere separati gli account pubblici e quelli di amministrazione, rifiutare qualsiasi cache condivisa per le pagine dei membri e considerare le email come non consegnate finché non esiste alcuna conferma.
