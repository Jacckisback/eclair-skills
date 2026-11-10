# Plano de validação — Conteúdos relacionados

## Modelo de dados
Conteúdo, categoria, palavras comuns, lista de ligações calculada.

## Implementação esperada
Calcular as associações no momento da publicação ou por tarefa, apresentá-las através de um bloco estático armazenável em cache, limitar a algumas ligações.

## Testes a prever
1. Nominal: Verificar as ligações propostas em vários artigos de categorias diferentes.
2. Controlo de recusa: Um artigo eliminado deixa de ser proposto após a regeneração.
3. Invariante: Nenhuma associação aponta para um conteúdo não publicado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
