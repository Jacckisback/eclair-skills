# Plano de validação — Línguas da direita para a esquerda

## Modelo de dados
Direção do texto, propriedades lógicas CSS, ícones orientados.

## Implementação esperada
Utilizar as propriedades lógicas CSS no tema de site, testar cada modelo em dir=rtl.

## Testes a prever
1. Nominal: Apresentar as páginas-tipo da direita para a esquerda sem transbordo.
2. Controlo de recusa: Uma mistura de línguas não quebra a ordem de leitura.
3. Invariante: Nenhum texto de utilizador é injetado sem escape, incluindo os caracteres de direção.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
