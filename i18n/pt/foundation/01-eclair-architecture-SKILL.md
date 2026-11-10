---
name: eclair-architecture
description: Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC.
---

# Éclair Architecture — preservar o núcleo v2

## Objetivo
Conceber a solução pedida **sem copiar um sistema de extensões** e sem sobrecarregar a rota de cache. Começar por `references/core-map.md` e pelo código do checkout atual.

## Sequência operacional
1. Registar o commit, a versão `ECLAIR_VERSION`, o PHP e as capacidades disponíveis através de `/admin/api/capabilities` se o acesso for autorizado.
2. Classificar o objetivo: conteúdo/definição nativa, tema do site, extensão `eclair-extension/1`, serviço externo, ou lacuna do contrato público que necessita de uma RFC.
3. Procurar primeiro `Extensions`, `Themes`, `Packages`, `Migrations`, `Store`, `Cache`, `Site`, `Seo`, `Security`, `Mcp` e os docs `docs/ARCHITECTURE-2.md`/`docs/STATUS-2.md`.
4. Descrever as fronteiras: código sob `site/extensions/` ou `site/themes/`, dados via `Store` e `$ctx['data']`, média sob `media/`, nenhuma substituição de `app/`.
5. Distinguir estritamente o contrato nativo (`eclair-extension/1`) das antigas experiências v0.8 (rotas/permissões/SQL/outbox), incompatíveis com a v2 sem portabilidade.
6. Produzir uma decisão de arquitetura explícita: alternativas, limites da API, riscos, rollback, teste de compatibilidade e indicadores de desempenho.
7. Mandar rever e depois validar com `php tests/run.php`, `php tools/measure.php --check` e os testes pertinentes de `tests/extensions.php`.

## Não negociáveis
Preservar SEO/GEO, marcação canónica, proteções CSRF/CSP, gestão da autenticação e cache quente. Uma extensão nunca se ativa a si própria. Não pretender gerir um checkout transacional, nem as contas de alunos, enquanto esses contratos não estiverem implementados e testados.

## Entregáveis
ADR e cartografia antes/depois, decisão «native / extension / core RFC», restrições, testes e plano de reversão. O modelo `assets/architecture-decision.md` pode servir de ponto de partida.

## V1.0 — Extensões de membros
A extensão nativa `examples/extensions/member-directory` ilustra as contas públicas separadas: nenhum novo papel em `Eclair\Users`. Um núcleo 2.0 recebe as extensões através de `site/extensions/<id>`; nenhuma escrita em `app/`.

## Éclair 2.0 — protótipo v1.1 (experimental)
O Éclair 2.0.0 possui agora um contrato experimental de POST público apenas se o patch v1.1 for aplicado num ramo de desenvolvimento. O núcleo oficial **não** fornece este contrato. Nenhuma modificação direta do núcleo a partir de um skill; preparação de uma RFC e testes prévios.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
