# Plano de validação — Revista e atualidade

## Modelo de dados
Artigo, secção, autor, primeira página, data.

## Implementação esperada
Estruturar secções e primeira página, cuidar de autores e datas, utilizar as funcionalidades nativas para os média (imagens grandes, agendamento, feeds).

## Testes a prever
1. Nominal: Publicar uma primeira página de teste e verificar secções, feeds e sitemap.
2. Controlo de recusa: Um artigo corrigido apresenta a sua data de atualização.
3. Invariante: Nenhuma informação sem fonte apresentada como um facto.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
