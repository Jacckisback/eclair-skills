# Plano de validação — Cookies e consentimento

## Modelo de dados
Rastreador, finalidade, consentimento, prova.

## Implementação esperada
Inventariar os rastreadores reais; sem rastreador, sem faixa de cookies; caso contrário, consentimento prévio, recusa tão simples quanto a aceitação e página de informação.

## Testes a prever
1. Nominal: Inspecionar cookies e pedidos antes e depois da escolha.
2. Controlo de recusa: Após uma recusa, nenhum rastreador de terceiros é carregado.
3. Invariante: Nenhum rastreador sujeito a consentimento é instalado antes da aceitação.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
