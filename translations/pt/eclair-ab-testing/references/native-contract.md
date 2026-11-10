# Aplicação do contrato nativo ao skill eclair-ab-testing

Este skill utiliza exclusivamente o que o Éclair CMS 2.0.x entrega: as funcionalidades do núcleo, o contrato de tema e o contrato `eclair-extension/1`. Referência oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posição deste skill

Esta funcionalidade requer escritas de visitantes, contas públicas, transações ou eventos assinados que `eclair-extension/1` não fornece na 2.0. Entregar a conceção, uma maqueta GET segura e testes bloqueantes; nunca anunciar uma colocação em produção.

## Salvaguarda prática

Num checkout real, reler `eclair/index.php`, executar `php tools/validate.php` sobre qualquer pacote produzido e `php tests/run.php`. Se o pedido ultrapassar as funcionalidades nativas, as rotas GET públicas, as páginas de administração protegidas, os blocos, as definições e `Store`, produzir um pedido de evolução distinto; **nunca simular a sua disponibilidade**.
