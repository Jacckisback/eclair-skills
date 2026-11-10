# Plano de validação — Artigos de blogue

## Modelo de dados
Artigo, excerto, imagem principal, categoria, autor, data, estado rascunho ou publicado.

## Implementação esperada
Criar os artigos em rascunho através da administração ou do conector MCP, verificar título, excerto, imagem e categoria e, depois, deixar que uma pessoa publique.

## Testes a prever
1. Nominal: Criar um rascunho completo, pedir a sua publicação e, depois, verificar a apresentação, o feed RSS e o sitemap.
2. Controlo de recusa: Um rascunho não aparece no site público, nem no sitemap, nem no feed.
3. Invariante: Nunca publicar nem eliminar um conteúdo em vez da pessoa autorizada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
