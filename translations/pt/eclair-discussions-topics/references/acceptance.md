# Plano de validação — Tópicos e respostas

## Modelo de dados
Tópico, resposta, versão, autor, carimbo temporal, afixado, fechado, eliminado.

## Implementação esperada
Definir parentesco das respostas, paginação, histórico das edições, menções e permalinks; tratar envios idempotentes.

## Testes a prever
1. Nominal: Testar respostas concorrentes, mensagem apagada e tópico fechado.
2. Controlo de recusa: Um membro não consegue editar nem eliminar a resposta de outro sem direito explícito.
3. Invariante: Escapar Markdown/HTML e verificar a permissão de editar para cada publicação.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
