---
name: eclair-test-suite
description: Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations.
---

# Éclair Test Suite — uma prova antes da publicação

## Ordem de verificação
1. Registar o commit e o `ECLAIR_VERSION`; exigir o contrato v2 oficial. Sem checkout completo, limitar a afirmação aos testes realmente executáveis.
2. `php -l` de cada PHP produzido e depois `php tools/validate.php site/extensions/<id> --json` com o núcleo correspondente.
3. `php tests/run.php --unit`, depois `php tests/run.php` (HTTP, auth, rotas, cache, cópias de segurança, extensões, temas, migração WordPress).
4. `php tools/measure.php --check`; comparar a cache quente e o orçamento de memória/tempo com o núcleo não modificado.
5. Testar instalação inativa, ativação, migração idempotente, update, conflito de rota, desativação, conservação dos dados, eliminação de código e eventual purga manual.
6. Se houver contas de membros/SQL: exigir testes PHP/PDO reais, multiprocesso, autorizações por objeto, webhooks assinados e restauro a partir de cópia de segurança. `pdo_sqlite` ausente = teste bloqueado, não aprovado.
7. CI recomendada: matriz PHP 8.1 a 8.5, `tests.yml` oficial, arquivo construído e servidores Apache/Nginx; acrescentar jobs específicos da funcionalidade.
8. Produzir uma tabela de testes executados / falhados / bloqueados. Nunca reportar «compatível com produção» a partir de uma fixture isolada.

## Entregáveis
Scripts e fixtures, relatório de execução, cobertura dos casos adversos, orçamentos e estratégia de rollback.

## V1.0 — Verificações suplementares
Executar `php tests/member-directory.php`, `python3 -m unittest discover -s tests -v` e `python3 scripts/verify_sample.py`. Num checkout Éclair 2.0 completo, executar **imperativamente** `php tools/validate.php examples/extensions/member-directory --json` e depois os testes PHP/HTTP do CMS completo e o orçamento `tools/measure.php --check` antes de qualquer proposta de fusão.

## Éclair 2.0 — protótipo v1.1 (experimental)
Testar `php tests/member-directory.php` + `php tests/member-public.php` e os testes Python. Num clone real do Éclair 2.0.0, aplicar o patch a uma feature branch limpa, executar `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` e ensaios HTTP/TLS. Nenhuma fusão sem estes critérios.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
