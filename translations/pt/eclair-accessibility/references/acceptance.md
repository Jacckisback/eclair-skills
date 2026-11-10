# Plano de validação — Acessibilidade WCAG

## Modelo de dados
Estrutura dos títulos, navegação por teclado, foco, formulários, multimédia, contrastes.

## Implementação esperada
Realizar uma auditoria com teclado e leitor de ecrã, verificar axe-core, contrastes, mensagens de erro e movimento reduzido.

## Testes a prever
1. Nominal: Testar percursos sem rato, erros de formulário e zoom a 200%.
2. Controlo de recusa: Um formulário permanece compreensível sem cor e a partir do teclado.
3. Invariante: Não suprimir o foco visível nem tornar uma funcionalidade dependente unicamente da cor ou de um gesto.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
