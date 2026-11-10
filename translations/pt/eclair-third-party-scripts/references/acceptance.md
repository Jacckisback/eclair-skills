# Plano de validação — Scripts de terceiros

## Modelo de dados
Script, finalidade, peso, domínio, consentimento exigido.

## Implementação esperada
Inventariar cada pedido de script, procurar uma alternativa sem script, documentar o bloqueio pela política de conteúdo nativa quando existir.

## Testes a prever
1. Nominal: Medir peso e pedidos antes e depois de cada adição aceite.
2. Controlo de recusa: Um script de um domínio não autorizado não é executado.
3. Invariante: Nenhum script é injetado contornando a Content-Security-Policy.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
