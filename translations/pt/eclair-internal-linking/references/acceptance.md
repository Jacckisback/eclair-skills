# Plano de validação — Ligações internas

## Modelo de dados
Página de origem, página de destino, âncora, páginas órfãs.

## Implementação esperada
Mapear as ligações, identificar as páginas órfãs, adicionar ligações úteis com âncoras descritivas.

## Testes a prever
1. Nominal: Verificar que cada página importante recebe pelo menos uma ligação interna.
2. Controlo de recusa: Nenhuma ligação interna aponta para um redirecionamento ou para um erro.
3. Invariante: Nenhuma ligação é adicionada automaticamente sem revisão do contexto.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
