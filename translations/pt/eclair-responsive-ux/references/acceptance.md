# Plano de validação — UX responsiva

## Modelo de dados
Breakpoints, densidade, largura de texto, menu, formulários e multimédia.

## Implementação esperada
Conceber em mobile-first; manter a hierarquia da informação; testar ecrãs pequenos, tamanhos dos alvos e orientações.

## Testes a prever
1. Nominal: Testar 320px, 375px, tablet e teclado móvel.
2. Controlo de recusa: Uma ação primária permanece visível e utilizável num ecrã estreito sem scroll horizontal.
3. Invariante: Nenhum conteúdo essencial oculto em dispositivos móveis ou dependente de animação.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
