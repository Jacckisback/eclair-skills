# Plano de validação — Cache de páginas

## Modelo de dados
Página em cache, invalidação, variantes proibidas.

## Implementação esperada
Medir a resposta em cache, identificar o que impede a colocação em cache de uma rota de extensão, verificar a invalidação na modificação.

## Testes a prever
1. Nominal: Medir o tempo de resposta antes e depois de uma modificação.
2. Controlo de recusa: Uma rota de extensão declarada como não colocável em cache nunca é servida a partir da cache.
3. Invariante: Nenhuma página que contenha dados de sessão ou pessoais entra na cache partilhada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
