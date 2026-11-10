# Plano de validação — Reservas de atividade

## Modelo de dados
Recurso, intervalo, capacidade, fuso horário, estado e reserva.

## Implementação esperada
Definir regras de disponibilidade e cancelamento, bloquear os horários de forma transacional, distinguir opção e reserva firme.

## Testes a prever
1. Nominal: Testar clientes em simultâneo, mudanças de hora e cancelamento.
2. Controlo de recusa: Último lugar reservado em simultâneo => uma única confirmação.
3. Invariante: Nenhum calendário GET em cache substitui a validação transacional da disponibilidade.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
