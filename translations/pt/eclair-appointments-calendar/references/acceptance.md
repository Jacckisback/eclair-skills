# Plano de validação — Marcações e calendário

## Modelo de dados
Prestador, serviço, duração, buffers, exceções, eventos e fusos horários.

## Implementação esperada
Normalizar horários em UTC, conservar o fuso horário de apresentação, bloquear horários de indisponibilidade, gerir a ressincronização externa.

## Testes a prever
1. Nominal: Testar DST, marcação que atravessa a meia-noite, evento eliminado.
2. Controlo de recusa: Um horário bloqueado manualmente nunca é proposto após a ressincronização.
3. Invariante: Uma integração externa exige OAuth/scopes mínimos e não deve expor os calendários privados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
