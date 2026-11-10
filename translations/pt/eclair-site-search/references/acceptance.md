# Plano de validação — Pesquisa no site

## Modelo de dados
Índice dos conteúdos publicados, título, excerto, endereço.

## Implementação esperada
Gerar um índice estático dos conteúdos públicos por tarefa agendada, servi-lo em GET armazenável em cache e pesquisar do lado do navegador, com uma página de recurso sem JavaScript.

## Testes a prever
1. Nominal: Pesquisar um termo presente, ausente e acentuado e verificar o tempo de resposta.
2. Controlo de recusa: Um rascunho ou uma página privada nunca aparece no índice.
3. Invariante: O índice só contém conteúdos públicos; nenhuma consulta de visitante é registada com a sua identidade.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
