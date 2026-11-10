# Plano de validação — Direção artística Éclair

## Modelo de dados
Posicionamento, identidade, tipografia, cores, componentes, fotografias e conteúdo real.

## Implementação esperada
Definir um universo inspirado na atividade, compor secções, ajustar o CSS e testar os temas com conteúdo real; privilegiar site/themes e os blocos existentes.

## Testes a prever
1. Nominal: Testar o contraste, a coerência entre páginas e as versões móveis.
2. Controlo de recusa: A nova aparência permanece legível sem JavaScript e respeita as ligações existentes.
3. Invariante: Nunca modificar app/theme/ nem quebrar o SEO, a CSP ou o caminho rápido.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
