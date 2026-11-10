# Plano de validação — Modo escuro

## Modelo de dados
Conjuntos de cores claro e escuro, preferência do visitante.

## Implementação esperada
Definir as variáveis de cor do tema para prefers-color-scheme, verificar contrastes, imagens e logótipos.

## Testes a prever
1. Nominal: Verificar os contrastes dos dois modos nas páginas-tipo.
2. Controlo de recusa: Um logótipo escuro não se torna invisível em modo escuro.
3. Invariante: Não é necessário nenhum cookie para respeitar a preferência do sistema.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
