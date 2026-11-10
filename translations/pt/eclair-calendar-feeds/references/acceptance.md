# Plano de validação — Feeds de calendário

## Modelo de dados
Evento, data, fuso horário, local, feed iCalendar.

## Implementação esperada
Gerar um feed iCalendar público em GET a partir dos eventos publicados, com fusos horários explícitos.

## Testes a prever
1. Nominal: Subscrever o feed a partir de duas aplicações de calendário.
2. Controlo de recusa: Um evento cancelado é marcado como cancelado no feed.
3. Invariante: O feed contém apenas eventos públicos, sem participantes.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
