# Plano de validação — Início de sessão com conta de terceiros

## Modelo de dados
Fornecedor de identidade, conta associada, consentimento.

## Implementação esperada
Depende primeiro de contas de membro; conceber o fluxo OAuth com estado, PKCE e associação de conta explícita.

## Testes a prever
1. Nominal: Simular início de sessão, associação e desassociação.
2. Controlo de recusa: Uma resposta OAuth repetida ou falsificada é recusada.
3. Invariante: Nenhuma conta é fundida apenas com base num endereço de e-mail não verificado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
