# Plano de validação — Proteção do início de sessão

## Modelo de dados
Tentativas, limites por rede e por conta, endereço de administração.

## Implementação esperada
Controlar os limites de tentativas nativos, o endereço de administração, as sessões ativas e as palavras-passe provisórias.

## Testes a prever
1. Nominal: Simular falhas repetidas e constatar o bloqueio.
2. Controlo de recusa: O dispositivo habitual do proprietário não é bloqueado pelas tentativas de um terceiro.
3. Invariante: Nenhum limite nativo é relaxado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
