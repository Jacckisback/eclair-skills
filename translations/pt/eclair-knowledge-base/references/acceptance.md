# Plano de validação — Base de conhecimento

## Modelo de dados
Artigo de ajuda, secção, versão, data de atualização.

## Implementação esperada
Organizar por problemas dos utilizadores, uma resposta por página, navegação por secções e pesquisa interna.

## Testes a prever
1. Nominal: Resolver três problemas-tipo apenas com a documentação.
2. Controlo de recusa: Um artigo obsoleto é datado e assinalado, não deixado como válido.
3. Invariante: Nenhum procedimento não testado é publicado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
