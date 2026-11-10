# Plano de validação — Gestor de etiquetas

## Modelo de dados
Contentor, etiquetas, acionadores, consentimento.

## Implementação esperada
Listar as etiquetas realmente necessárias, procurar uma alternativa do lado do servidor, documentar o bloqueio pela política de conteúdo nativa.

## Testes a prever
1. Nominal: Fazer o inventário das etiquetas e da respetiva alternativa.
2. Controlo de recusa: Uma etiqueta não justificada não é adicionada.
3. Invariante: Nenhum contentor que permita injetar código arbitrário sem revisão.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
