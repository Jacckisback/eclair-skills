# Plano de validação — Títulos e meta-descrições

## Modelo de dados
Título, meta-descrição, expressão visada, pré-visualização do resultado.

## Implementação esperada
Redigir para cada página um título e uma descrição únicos, recorrer à pontuação em tempo real do editor sem a tratar como um objetivo.

## Testes a prever
1. Nominal: Verificar a unicidade e o comprimento em todas as páginas.
2. Controlo de recusa: Duas páginas publicadas não têm o mesmo título.
3. Invariante: Nenhuma promessa de posição; nenhum excesso de palavras-chave.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
