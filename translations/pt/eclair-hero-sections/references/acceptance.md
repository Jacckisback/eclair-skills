# Plano de validação — Secções de abertura

## Modelo de dados
Título, subtítulo, imagem, botão.

## Implementação esperada
Escrever uma promessa precisa, escolher uma imagem leve, manter um único título principal e um botão.

## Testes a prever
1. Nominal: Medir a apresentação do maior elemento num dispositivo móvel.
2. Controlo de recusa: Sem imagem, a secção permanece legível e com contraste.
3. Invariante: A imagem principal tem dimensões explícitas e não atrasa a apresentação.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
