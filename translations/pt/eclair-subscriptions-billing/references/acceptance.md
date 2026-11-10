# Plano de validação — Subscrições pagas

## Modelo de dados
Oferta, período, subscritor, data de vencimento, estado.

## Implementação esperada
Deixar o prestador gerir as cobranças e a área de cliente; conceber a sincronização das permissões por eventos assinados.

## Testes a prever
1. Nominal: Simular subscrição, renovação, falha e rescisão.
2. Controlo de recusa: Um pagamento falhado não prolonga nenhum acesso.
3. Invariante: Uma permissão de acesso só é aberta com base num evento de pagamento autenticado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
