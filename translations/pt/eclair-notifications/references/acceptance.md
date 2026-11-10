# Plano de validação — Notificações de comunidade

## Modelo de dados
Subscrição, menção, notificação, canal, preferência, estado.

## Implementação esperada
Emitir eventos após escrita validada, filtrar por direitos no momento da leitura e do envio, aplicar o cancelamento da subscrição.

## Testes a prever
1. Nominal: Testar notificações repetidas, cancelamento da subscrição e retirada de permissão.
2. Controlo de recusa: Após a revogação do acesso, nenhuma nova notificação contém um excerto privado.
3. Invariante: Nunca revelar conteúdo de categorias privadas em email, push ou digest.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
