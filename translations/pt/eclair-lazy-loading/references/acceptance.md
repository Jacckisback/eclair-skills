# Plano de validação — Carregamento diferido

## Modelo de dados
Imagem, prioridade, dimensões.

## Implementação esperada
Verificar que a imagem principal é carregada com prioridade e as restantes em diferido, com dimensões explícitas.

## Testes a prever
1. Nominal: Medir a apresentação do maior elemento e o deslocamento do layout.
2. Controlo de recusa: A imagem principal nunca é carregada em diferido.
3. Invariante: Nenhum script de terceiros é adicionado para diferir o carregamento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
