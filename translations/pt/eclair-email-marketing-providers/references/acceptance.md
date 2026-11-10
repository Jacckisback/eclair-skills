# Plano de validação — Serviços de e-mail marketing

## Modelo de dados
Lista, formulário alojado, chave de API, sincronização.

## Implementação esperada
Utilizar o formulário alojado do serviço; guardar qualquer chave de API nos segredos da extensão; sincronizar por tarefa se necessário.

## Testes a prever
1. Nominal: Inscrever um endereço de teste e reencontrá-lo no serviço.
2. Controlo de recusa: Uma chave revogada produz um erro registado, não uma fuga.
3. Invariante: Nenhuma chave de API no código, no repositório ou numa página pública.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
