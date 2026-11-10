# Plano de validação — Páginas do site

## Modelo de dados
Página, endereço, blocos, página-mãe, estado, entrada de menu.

## Implementação esperada
Listar as páginas necessárias, fixar os endereços antes da redação, compor cada página em blocos e ligar as páginas entre si.

## Testes a prever
1. Nominal: Criar a estrutura em árvore completa e verificar cada endereço, o menu e o trilho de navegação.
2. Controlo de recusa: Uma página renomeada responde com um único redirecionamento 301, nunca com um erro 404.
3. Invariante: Nunca alterar o endereço de uma página publicada sem um redirecionamento verificado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
