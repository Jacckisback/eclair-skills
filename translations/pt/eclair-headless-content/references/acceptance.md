# Plano de validação — Conteúdo para aplicações e IA

## Modelo de dados
Versão Markdown, llms.txt, feeds, sitemap.

## Implementação esperada
Apoiar-se nas saídas nativas legíveis por máquina, documentar o seu formato e a sua atualidade para a aplicação cliente.

## Testes a prever
1. Nominal: Ler uma página em HTML e em Markdown e comparar.
2. Controlo de recusa: Um rascunho não tem versão Markdown acessível.
3. Invariante: Nenhum conteúdo privado é exposto por estas saídas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
