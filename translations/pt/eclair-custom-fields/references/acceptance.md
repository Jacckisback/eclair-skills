# Plano de validação — Campos personalizados

## Modelo de dados
Campo, tipo declarado, valor validado, bloco ou definição de suporte.

## Implementação esperada
Declarar os campos no manifesto (tipos suportados pelo núcleo), deixar o núcleo validar e armazenar, apresentar com escape.

## Testes a prever
1. Nominal: Declarar um bloco com campos de texto, número e escolha e, depois, verificar a validação e a apresentação.
2. Controlo de recusa: Um valor fora do formato é recusado pelo núcleo e nunca chega à apresentação.
3. Invariante: Qualquer valor apresentado passa por e(); nenhum campo contém segredos.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
