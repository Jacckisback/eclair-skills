# Plano de validação — Distintivos e pontos

## Modelo de dados
Regra, pontos, distintivo, classificação.

## Implementação esperada
Fixar regras simples e verificáveis do lado do servidor, prever a retirada em caso de abuso e a opção de não aparecer na classificação.

## Testes a prever
1. Nominal: Simular ganho, retirada e apresentação da classificação.
2. Controlo de recusa: Uma ação repetida artificialmente não rende pontos em duplicado.
3. Invariante: Nenhum ponto é atribuído com base numa informação enviada pelo navegador.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
