# Plano de validação — Painel pedagógico

## Modelo de dados
Inscrições, progresso, resultados agregados, eventos de curso.

## Implementação esperada
Definir métricas úteis aos formadores, filtrar por curso e autorização; reduzir a recolha; prever retenção e exportação.

## Testes a prever
1. Nominal: Testar visibilidade do formador no curso A vs B.
2. Controlo de recusa: Um pedido de estatísticas agregadas não deve expor a identidade de um estudante terceiro.
3. Invariante: As estatísticas de um aluno só são visíveis para as partes autorizadas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
