# Plano de validação — Devoluções e reembolsos

## Modelo de dados
Pedido de devolução, motivo, estado, reembolso.

## Implementação esperada
Publicar a política de devolução nativa nas fichas, tratar os pedidos pelo formulário de contacto, reembolsar junto do prestador; conceber o acompanhamento estruturado.

## Testes a prever
1. Nominal: Percorrer um pedido de devolução da receção ao reembolso.
2. Controlo de recusa: Um pedido fora de prazo recebe uma resposta fundamentada, não um reembolso automático.
3. Invariante: Um reembolso só é desencadeado por uma pessoa habilitada, junto do prestador.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
