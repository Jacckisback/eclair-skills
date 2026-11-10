---
name: eclair-cache-contract
description: Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets.
---

# Éclair Cache Contract — manter a cache segura

## Decisão
1. Ler `eclair/index.php`, `Cache.php`, `Extensions::route()` e `docs/EXTENSION-CONTRACT.md` do núcleo v2 visado.
2. Para as páginas de extensão com conteúdo público idêntico para todos, `routes.public[].cache` pode ser `true` após verificação das dependências de renderização.
3. Para conteúdos privados, estados de utilizador, carrinhos, tokens ou preços personalizados: **sem cache partilhada** (`Cache-Control: private, no-store`), `noindex` pertinente e contrato de autenticação de servidor. Nunca pretender que um `cache:false` implementa por si só a autenticação.
4. Medir GET/HEAD e query strings, primeira geração e depois cache HIT, edição dos dados, ativação/desativação e migrações. Verificar as rotas CMS e o índice `data/ext-public.php`.
5. Nunca acrescentar lookup nem leitura de registo ao caminho rápido `index.php` sem um orçamento medido e uma justificação de segurança.
6. Testar `php tools/measure.php --check` e os orçamentos em `tools/budgets.json`, depois comparar com um baseline limpo com a mesma versão de PHP e os mesmos dados.
7. Verificar a purga após ativação e que as páginas públicas não abrangidas continuam colocáveis em cache; testar cookies e cabeçalhos em situação concorrente.

## Entregáveis
Matriz URL × método × identidade × cache, medições e testes de isolamento.

## V1.0 — Identidade e cache
Nunca servir uma página personalizada a partir de uma cache partilhada. As rotas de administrador existentes já são `private, no-store`; as futuras páginas públicas de membros necessitam de um contrato de rota privada antes de qualquer abertura. Nunca supor que `cache:false` implementa automaticamente garantias completas de sessão/CSRF.

## Éclair 2.0 — protótipo v1.1 (experimental)
Os formulários públicos GET utilizam `Security::formField()` e devem ser declarados `cache:false`. As suas respostas não devem atingir o fast path do núcleo. POST é excluído do fast path e forçado a no-store. Testar a purga na ativação do módulo e verificar a ausência de cookies/identidades no HTML de cache partilhada.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
