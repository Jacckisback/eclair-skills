# Plano de validação — Cronologias

## Modelo de dados
Etapa, data, título, texto.

## Implementação esperada
Apresentar a cronologia como lista ordenada estilizada em CSS, legível em coluna em dispositivos móveis.

## Testes a prever
1. Nominal: Verificar a ordem de leitura e a apresentação em dispositivos móveis.
2. Controlo de recusa: Uma etapa sem data permanece legível e ordenada.
3. Invariante: As datas e os factos apresentados são fornecidos pelo cliente.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
