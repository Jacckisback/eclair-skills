# Plano de validação — Criação de percursos

## Modelo de dados
Curso, módulo, lição, ordem, rascunho, versão publicada e autor.

## Implementação esperada
Estabelecer esquema hierárquico; pré-visualizar antes da publicação; preservar os identificadores na reordenação; documentar o arquivamento.

## Testes a prever
1. Nominal: Testar troca de lições, despublicação e edição concorrente.
2. Controlo de recusa: Alterar a ordem não reinicia o progresso dos estudantes.
3. Invariante: Os rascunhos de formador não devem ser indexados nem expostos publicamente.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
