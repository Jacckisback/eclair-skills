# Aplicação do contrato nativo ao skill eclair-storage

Este skill utiliza exclusivamente o contrato `eclair-extension/1` entregue no Éclair CMS 2.0.0 e não as API dos antigos protótipos. Referência oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Salvaguarda prática

Num checkout real, reler `eclair/index.php`, executar `php tools/validate.php` sobre qualquer pacote produzido e `php tests/run.php`. Se o contrato pedido ultrapassar as rotas GET públicas, as permissões admin, os campos/blocos e `Store`, produzir uma RFC distinta; **nunca simular a sua disponibilidade**.
