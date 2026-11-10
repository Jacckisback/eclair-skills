# Plano de validação — Registo de atividade

## Modelo de dados
Evento, conta, data, ação.

## Implementação esperada
Consultar o registo da página Segurança, identificar inícios de sessão e alterações sensíveis, fixar uma rotina de controlo.

## Testes a prever
1. Nominal: Provocar uma ação sensível e reencontrá-la no registo.
2. Controlo de recusa: Uma conta sem o direito Segurança não acede ao registo.
3. Invariante: O registo só é legível pelas contas que têm o direito Segurança.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
