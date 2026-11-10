# Plano de validação — Visualizador de imagens

## Modelo de dados
Imagem, versão ampliada, legenda.

## Implementação esperada
Utilizar dialog nativo ou ligação para a imagem, gerir o foco, a tecla Esc e o retorno, sem dependências.

## Testes a prever
1. Nominal: Abrir, navegar e fechar com o teclado.
2. Controlo de recusa: Sem JavaScript, o clique abre simplesmente a imagem.
3. Invariante: O foco é retido e depois devolvido corretamente; nenhum conteúdo externo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
