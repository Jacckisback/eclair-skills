# Plano de validação — Catálogo de produtos

## Modelo de dados
Produto, SKU, slug, título, descrição, preço de apresentação, multimédia, disponibilidade e categoria.

## Implementação esperada
Prototipar primeiro uma página pública GET armazenável em cache; produzir um esquema de produto e o respetivo índice; manter os títulos e as descrições de origem; definir paginação e canonical; preservar os slugs ao longo das edições.

## Testes a prever
1. Nominal: Testar categorias, listas vazias, URL canónico, pesquisa e eliminação soft.
2. Controlo de recusa: Um produto eliminado ou privado não deve permanecer no catálogo nem numa cache antiga.
3. Invariante: O preço apresentado nunca é tomado como fonte de autoridade numa futura encomenda.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
