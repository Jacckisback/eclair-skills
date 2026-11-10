# Plano de validação — Tipos de letra

## Modelo de dados
Tipo de letra, pesos, ficheiro autoalojado, alternativa de sistema.

## Implementação esperada
Utilizar os tipos de letra do sistema ou o tipo de letra de título autoalojado das direções artísticas, limitar os pesos.

## Testes a prever
1. Nominal: Verificar a ausência de pedidos a terceiros e de salto de texto.
2. Controlo de recusa: Um tipo de letra indisponível deixa uma alternativa legível.
3. Invariante: Nenhum tipo de letra é carregado a partir de um serviço de terceiros.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
