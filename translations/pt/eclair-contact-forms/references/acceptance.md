# Plano de validação — Formulário de contacto

## Modelo de dados
Mensagem, nome, e-mail, assunto, data, estado de leitura.

## Implementação esperada
Colocar o bloco de contacto nativo, definir o destinatário, testar o envio e a receção, apresentar a menção informativa.

## Testes a prever
1. Nominal: Enviar uma mensagem real e encontrá-la na administração e por e-mail.
2. Controlo de recusa: Os envios repetidos em rajada são limitados pelo núcleo.
3. Invariante: As mensagens só são visíveis para as contas com a permissão Mensagens.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
