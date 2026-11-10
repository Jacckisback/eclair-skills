# Plano de validação — Galerias de imagens

## Modelo de dados
Galeria, imagens, legendas, ordem.

## Implementação esperada
Compor a galeria em grelha CSS a partir das imagens da biblioteca multimédia, com legendas e textos alternativos.

## Testes a prever
1. Nominal: Apresentar uma galeria de vinte imagens num dispositivo móvel e medir o seu peso.
2. Controlo de recusa: Uma imagem retirada da biblioteca multimédia não deixa uma miniatura quebrada.
3. Invariante: Nenhuma imagem é carregada a partir de um domínio de terceiros.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
