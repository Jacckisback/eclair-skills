# Plano de validação — Documentos PDF

## Modelo de dados
Documento, título, resumo, página de apresentação, ficheiro.

## Implementação esperada
Criar uma página HTML de apresentação por documento com resumo, ligação de transferência e alternativa acessível.

## Testes a prever
1. Nominal: Verificar a ligação, o peso, o título do documento e a página de apresentação.
2. Controlo de recusa: Um PDF retirado devolve uma resposta limpa e não uma ligação quebrada nas páginas.
3. Invariante: Nenhum PDF que contenha dados pessoais é publicado sem consentimento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
