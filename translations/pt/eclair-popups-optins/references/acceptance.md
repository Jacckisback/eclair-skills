# Plano de validação — Janelas e caixas de incentivo

## Modelo de dados
Mensagem, acionador, frequência, ação.

## Implementação esperada
Preferir uma caixa inserida na página; caso contrário, dialog nativo acionado por uma ação do visitante, que se pode fechar com o teclado, nunca à chegada.

## Testes a prever
1. Nominal: Abrir e fechar com o teclado e em dispositivos móveis.
2. Controlo de recusa: A caixa recusada não reaparece durante a visita.
3. Invariante: Nenhuma janela bloqueia o conteúdo nem retém o foco.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
