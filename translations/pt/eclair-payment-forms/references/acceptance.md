# Plano de validação — Formulários de pagamento

## Modelo de dados
Serviço, montante, ligação de pagamento do prestador.

## Implementação esperada
Criar a ligação junto do prestador de serviços de pagamento, apresentá-la numa página clara com as condições, não armazenar nada no site.

## Testes a prever
1. Nominal: Pagar em modo de teste e verificar o recibo e a página de retorno.
2. Controlo de recusa: Um montante modificado do lado do navegador não tem qualquer efeito sobre o montante cobrado.
3. Invariante: Nenhum dado bancário transita nem é armazenado no site.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
