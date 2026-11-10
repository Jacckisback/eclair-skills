# Plano de validação — Etiquetas e taxonomias

## Modelo de dados
Termo, tipo de taxonomia, conteúdos ligados, endereço de arquivo.

## Implementação esperada
Inventariar as taxonomias existentes, fundir as que duplicam as categorias, propor páginas de agrupamento em GET para as restantes e redirecionar os arquivos antigos.

## Testes a prever
1. Nominal: Converter um conjunto de etiquetas em categorias ou em páginas de agrupamento e verificar os redirecionamentos.
2. Controlo de recusa: Um antigo arquivo de etiqueta eliminado redireciona para a página mais próxima, sem cadeia.
3. Invariante: Não gerar centenas de arquivos pobres indexáveis.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
