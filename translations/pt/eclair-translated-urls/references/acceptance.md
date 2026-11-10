# Plano de validação — Endereços traduzidos

## Modelo de dados
Endereço por língua, redirecionamentos, canonical, hreflang.

## Implementação esperada
Fixar uma convenção de endereços por língua, traduzir os slugs antes da publicação, verificar canonical e hreflang produzidos pelo núcleo.

## Testes a prever
1. Nominal: Verificar canonical e hreflang de cada versão.
2. Controlo de recusa: Duas línguas nunca partilham o mesmo endereço.
3. Invariante: Nenhum endereço publicado é alterado sem redirecionamento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
