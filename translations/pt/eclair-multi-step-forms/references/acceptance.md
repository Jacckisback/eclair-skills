# Plano de validação — Formulários em várias etapas

## Modelo de dados
Etapa, campos, validação, rascunho de resposta.

## Implementação esperada
Dividir por tema, validar do lado do servidor em cada etapa, prever a retoma e um resumo antes do envio.

## Testes a prever
1. Nominal: Preencher, voltar atrás, corrigir e enviar.
2. Controlo de recusa: Uma etapa inválida bloqueia a continuação e nenhum dado incompleto é transmitido.
3. Invariante: Nenhum dado parcial é conservado sem que a pessoa seja informada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
