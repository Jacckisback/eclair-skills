# Aplicação do contrato nativo ao skill eclair-cart-checkout

Este skill utiliza exclusivamente o que o Éclair CMS 2.0.x entrega: as funcionalidades do núcleo, o contrato de tema e o contrato `eclair-extension/1`. Referência oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posição deste skill

O núcleo já fornece uma loja leve (fichas de produto, variantes, categorias, ligações de pagamento de um prestador, feed de comerciante): utilizá-la primeiro, sem a duplicar. Para além disso, carrinho, encomendas e pagamentos precisam de POST públicos, de um armazenamento transacional fiável, de webhooks autenticados e de idempotência; o Éclair 2.0 oficial não fornece tudo isso. A PR #19 ainda é um rascunho: nunca utilizar uma rota POST não fundida como prova de compatibilidade.

## Salvaguarda prática

Num checkout real, reler `eclair/index.php`, executar `php tools/validate.php` sobre qualquer pacote produzido e `php tests/run.php`. Se o pedido ultrapassar as funcionalidades nativas, as rotas GET públicas, as páginas de administração protegidas, os blocos, as definições e `Store`, produzir um pedido de evolução distinto; **nunca simular a sua disponibilidade**.
