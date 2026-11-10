# Plano de validação — Otimização das imagens

## Modelo de dados
Imagem de origem, variantes responsivas, dimensões, peso.

## Implementação esperada
Fornecer imagens de origem com o tamanho adequado, deixar o núcleo produzir as variantes, verificar o peso real servido em dispositivos móveis.

## Testes a prever
1. Nominal: Medir o peso e as dimensões servidos em dispositivos móveis e em computador.
2. Controlo de recusa: Nenhuma imagem é servida sem dimensões explícitas.
3. Invariante: Os metadados sensíveis (geolocalização) não são publicados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
