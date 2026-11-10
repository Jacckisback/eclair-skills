# Plano de validação — Pré-visualizações de partilha

## Modelo de dados
Título de partilha, descrição, imagem de partilha.

## Implementação esperada
Verificar as etiquetas de partilha e a imagem gerada pelo núcleo, testar a pré-visualização nas principais plataformas.

## Testes a prever
1. Nominal: Testar a pré-visualização de um artigo e de uma página.
2. Controlo de recusa: Uma página sem imagem dedicada mantém uma pré-visualização predefinida correta.
3. Invariante: A imagem de partilha não contém nenhum dado pessoal nem texto enganador.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
