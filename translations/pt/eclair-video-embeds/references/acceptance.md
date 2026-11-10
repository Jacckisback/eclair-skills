# Plano de validação — Vídeos

## Modelo de dados
Vídeo, origem, imagem de pré-visualização, legendas.

## Implementação esperada
Utilizar o bloco de vídeo nativo, preferir uma fachada clicável para as plataformas de terceiros, fornecer legendas ou transcrição.

## Testes a prever
1. Nominal: Verificar que nenhum pedido a terceiros é emitido antes do clique.
2. Controlo de recusa: Um endereço de vídeo de um domínio não autorizado é recusado.
3. Invariante: Nenhum leitor de terceiros é carregado antes do clique do visitante.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
