# Aplicação do contrato nativo ao skill eclair-translated-urls

Este skill utiliza exclusivamente o que o Éclair CMS 2.0.x entrega: as funcionalidades do núcleo, o contrato de tema e o contrato `eclair-extension/1`. Referência oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posição deste skill

Uma parte depende de um ponto de extensão ausente do contrato 2.0 (tipos de conteúdo, contribuição SEO ou JSON-LD, política de conteúdo por funcionalidade, filtro de renderização). Entregar a parte nativa e documentar com precisão a lacuna, sem soluções de contorno.

## Salvaguarda prática

Num checkout real, reler `eclair/index.php`, executar `php tools/validate.php` sobre qualquer pacote produzido e `php tests/run.php`. Se o pedido ultrapassar as funcionalidades nativas, as rotas GET públicas, as páginas de administração protegidas, os blocos, as definições e `Store`, produzir um pedido de evolução distinto; **nunca simular a sua disponibilidade**.
