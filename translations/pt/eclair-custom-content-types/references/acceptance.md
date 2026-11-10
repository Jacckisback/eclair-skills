# Plano de validação — Tipos de conteúdo personalizados

## Modelo de dados
Ficha de negócio, campos, lista, endereço, estado.

## Implementação esperada
Escolher entre páginas com blocos dedicados e extensão com armazenamento próprio e rotas GET, fixar os endereços, prever lista e ficha.

## Testes a prever
1. Nominal: Criar um tipo de ficha por extensão, com lista e detalhe em GET, e depois validar o pacote.
2. Controlo de recusa: Uma ficha não publicada não é servida nem na lista nem pelo seu endereço direto.
3. Invariante: Nunca escrever nos ficheiros de conteúdos do núcleo a partir de uma extensão.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
