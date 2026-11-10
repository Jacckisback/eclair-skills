# Plano de validação — Seletor de língua

## Modelo de dados
Língua atual, versões disponíveis, rótulos.

## Implementação esperada
Listar as línguas pelo seu nome na própria língua, apontar para a versão equivalente, sem redirecionamento automático forçado.

## Testes a prever
1. Nominal: Mudar de língua a partir de uma página profunda e chegar à sua equivalente.
2. Controlo de recusa: Sem equivalente, a ligação conduz à página inicial da língua, não a um erro.
3. Invariante: Nenhum redirecionamento por endereço IP; a escolha do visitante é respeitada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
