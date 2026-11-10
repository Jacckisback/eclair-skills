# Plano de validação — Proteção contra o spam

## Modelo de dados
Mensagem, token de formulário, limite de frequência.

## Implementação esperada
Apoiar-se no token e nos limites do formulário nativo, adicionar se necessário um campo armadilha, vigiar a caixa de entrada.

## Testes a prever
1. Nominal: Enviar uma mensagem legítima e depois uma rajada automatizada.
2. Controlo de recusa: Um envio sem token válido é rejeitado.
3. Invariante: Nenhum serviço de terceiros recebe as mensagens dos visitantes sem informação prévia.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
