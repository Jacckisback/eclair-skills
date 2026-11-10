---
name: eclair-routing
description: Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility.
---

# Éclair Routing — proteger os URL e a compatibilidade

## Procedimento
1. Registar as rotas e os alias existentes, `Site.php`, `App.php`, `Aliases.php`, `Redirects.php`, `Content::byRoute`, e os URL reservados.
2. As rotas públicas de extensão `routes.public[]` são **apenas GET** e explicitamente enumeradas. Sem rota genérica `/{slug}` através de um manifesto inventado.
3. As rotas admin utilizam `routes.admin[]`, método GET/POST, sob `/<admin>/x/<id>/...` e com a permissão `right` nativa.
4. Testar antes da ativação as colisões com artigos/páginas/produtos, rotas reservadas, slug multilingue, site em subpasta e outras extensões.
5. Preservar o caminho exato de uma migração WordPress (barra final, .html, acentos) através dos mecanismos v2 `route`/`Aliases`, sem criar vários canonicals nem cascatas de 301.
6. Para uma funcionalidade que necessite de rotas públicas POST (checkout, API de cliente), documentar uma RFC/nova interface segura em vez de intercetar o núcleo ou de contornar o router.
7. Verificar canonicals, sitemap, JSON-LD, noindex para as interfaces privadas, `HEAD`, respostas 404/405 e cache.

## Entregáveis
Tabela das rotas, proprietário do namespace, plano de redirecionamentos, conflitos detetados e testes HTTP.

## V1.0 — Rota pública de início de sessão proibida
Os GET públicos declarativos do Éclair 2.0 são adequados a páginas públicas, **não** a um formulário POST de início de sessão. Nenhuma rota `/login` nem `/register` com efeitos secundários deve ser criada com GET. `member-directory` declara apenas rotas admin com permissão `users`.

## Éclair 2.0 — protótipo v1.1 (experimental)
As rotas públicas POST **não** estão presentes no Éclair 2.0 oficial. O patch proposto v1.1 faz uma exceção controlada: método POST explícito, `cache:false`, HTTPS, `Security::checkFormToken()`, resposta `private,no-store`, redirecionamento 303 relativo. Fazer sempre ensaios HTTP com o CMS completo antes da fusão.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
