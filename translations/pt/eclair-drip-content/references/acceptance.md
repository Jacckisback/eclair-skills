# Plano de validação — Desbloqueio progressivo

## Modelo de dados
Lição, regra de desbloqueio, data ou condição, inscrito.

## Implementação esperada
Descrever as regras (data, prazo após a inscrição, lição anterior), aplicá-las do lado do servidor a cada pedido.

## Testes a prever
1. Nominal: Simular a passagem do tempo e a validação de uma lição.
2. Controlo de recusa: Um endereço de lição bloqueada adivinhado não devolve o seu conteúdo.
3. Invariante: Uma lição bloqueada nunca é enviada para o navegador, mesmo oculta.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
