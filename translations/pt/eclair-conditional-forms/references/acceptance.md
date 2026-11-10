# Plano de validação — Formulários condicionais

## Modelo de dados
Campo, condição, ramo, validação.

## Implementação esperada
Descrever as regras em dados, aplicá-las do lado do servidor e do lado do navegador, testar cada ramo.

## Testes a prever
1. Nominal: Percorrer cada ramo até ao envio.
2. Controlo de recusa: Um campo obrigatório de um ramo ativo não pode ser contornado.
3. Invariante: A validação no servidor nunca confia nos campos ocultos do lado do navegador.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
