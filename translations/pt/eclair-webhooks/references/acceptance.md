# Plano de validação — Webhooks de entrada e de saída

## Modelo de dados
Origem, segredo, evento, assinatura, carimbo temporal, ID único, tentativa, resultado.

## Implementação esperada
Especificar contrato, verificar assinatura sobre os bytes em bruto, anti-repetição e fila durável; documentar retries/dlq e endpoint POST privado.

## Testes a prever
1. Nominal: Testar envio duplicado, atraso, ordem invertida e segredo alterado.
2. Controlo de recusa: Duas tentativas do mesmo webhook desencadeiam uma única mutação de negócio.
3. Invariante: Nunca publicar um webhook com segredo no URL nem tratar evento financeiro não assinado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
