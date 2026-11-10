# Plano de validação — Recuperação de carrinho abandonado

## Modelo de dados
Carrinho, contacto, consentimento, lembrete.

## Implementação esperada
Verificar a base legal, limitar o número de lembretes, apoiar-se nas ferramentas do prestador de pagamento quando existirem.

## Testes a prever
1. Nominal: Simular abandono, lembrete e cancelamento da subscrição.
2. Controlo de recusa: Um contacto que cancelou a subscrição não recebe nenhum lembrete.
3. Invariante: Nenhum lembrete sem consentimento ou base legal; cancelamento da subscrição imediato.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
