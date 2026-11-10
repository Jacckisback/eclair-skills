# Plano de validação — Conectores API

## Modelo de dados
OAuth/token, scopes, quotas, erros, paginação, versão e registos.

## Implementação esperada
Definir esquema de API, isolar segredos, validar esquemas de entrada, prever timeouts/circuit breaker e versionamento.

## Testes a prever
1. Nominal: Testar timeout, 429, 500, resposta malformada e revogação.
2. Controlo de recusa: Um 500 do fornecedor não danifica os dados locais nem a apresentação pública.
3. Invariante: Não permitir SSRF ou URLs dinâmicos arbitrários; nunca registar token nos registos.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
