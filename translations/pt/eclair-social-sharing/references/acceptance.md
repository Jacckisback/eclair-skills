# Plano de validação — Botões de partilha

## Modelo de dados
Rede, endereço de partilha, rótulo.

## Implementação esperada
Utilizar simples ligações de partilha e a API de partilha do navegador em melhoria progressiva.

## Testes a prever
1. Nominal: Partilhar uma página a partir de um dispositivo móvel e de um computador.
2. Controlo de recusa: Nenhum pedido a terceiros antes do clique.
3. Invariante: Nenhum botão carrega scripts ou rastreadores de terceiros.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
