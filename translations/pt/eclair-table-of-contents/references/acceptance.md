# Plano de validação — Índice automático

## Modelo de dados
Subtítulos, âncoras, níveis.

## Implementação esperada
Gerar o índice a partir dos subtítulos na renderização no servidor, com âncoras estáveis e sem JavaScript obrigatório.

## Testes a prever
1. Nominal: Verificar o índice num conteúdo com três níveis de subtítulos.
2. Controlo de recusa: Um conteúdo curto sem subtítulos não apresenta nenhum índice vazio.
3. Invariante: As âncoras geradas são escapadas e únicas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
