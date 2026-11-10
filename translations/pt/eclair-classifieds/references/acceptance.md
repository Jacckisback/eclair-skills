# Plano de validação — Classificados

## Modelo de dados
Anúncio, anunciante, categoria, estado, denúncia.

## Implementação esperada
Definir submissão, moderação, tempo de vida, denúncia e contacto entre as partes sem expor os dados de contacto.

## Testes a prever
1. Nominal: Simular submissão, moderação, expiração e denúncia.
2. Controlo de recusa: Um anúncio recusado ou expirado deixa de estar acessível.
3. Invariante: Nenhum anúncio publicado sem moderação; dados de contacto nunca apresentados em claro.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
