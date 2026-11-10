# Aplicação do contrato nativo ao skill eclair-discussions-topics

Este skill utiliza exclusivamente o que o Éclair CMS 2.0.x entrega: as funcionalidades do núcleo, o contrato de tema e o contrato `eclair-extension/1`. Referência oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posição deste skill

As categorias e listas públicas podem ser GET; publicações, denúncias, perfis privados e moderação exigem uma identidade e rotas de escrita seguras, antisspam e armazenamento adequado.

## Salvaguarda prática

Num checkout real, reler `eclair/index.php`, executar `php tools/validate.php` sobre qualquer pacote produzido e `php tests/run.php`. Se o pedido ultrapassar as funcionalidades nativas, as rotas GET públicas, as páginas de administração protegidas, os blocos, as definições e `Store`, produzir um pedido de evolução distinto; **nunca simular a sua disponibilidade**.
