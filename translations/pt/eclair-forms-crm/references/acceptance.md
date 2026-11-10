# Plano de validação — Formulários e mini-CRM

## Modelo de dados
Formulário, campo, consentimento, contacto, origem, ticket e estado.

## Implementação esperada
Definir finalidade e prazo de conservação por formulário; validar dados no servidor; proteger contra spam; isolar ficheiros e direito de leitura.

## Testes a prever
1. Nominal: Testar spam, anexo, duplicado e eliminação RGPD.
2. Controlo de recusa: Um utilizador sem direito não consegue exportar a base de contactos.
3. Invariante: Um formulário público não deve permitir injeção de email nem fazer aparecer os dados na cache.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
