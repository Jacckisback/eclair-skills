# Plano de validação — Fluxo editorial

## Modelo de dados
Rascunho, autor, revisor, data prevista, estado, entrada de planeamento.

## Implementação esperada
Fixar quem redige e quem publica de acordo com as permissões nativas, utilizar o planeamento editorial e os rascunhos, manter uma revisão humana antes de qualquer colocação em linha.

## Testes a prever
1. Nominal: Fazer passar um conteúdo da ideia ao rascunho e, depois, à publicação por uma pessoa habilitada.
2. Controlo de recusa: Uma conta limitada aos conteúdos não pode alterar as definições nem publicar em vez de outro papel.
3. Invariante: Um agente ou um redator sem permissão de publicação não coloca nada em linha.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
