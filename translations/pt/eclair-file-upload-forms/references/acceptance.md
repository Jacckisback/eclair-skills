# Plano de validação — Formulários com anexos

## Modelo de dados
Ficheiro enviado, tipo, tamanho, proprietário, prazo de conservação.

## Implementação esperada
Definir os tipos e tamanhos aceites, armazenamento fora da raiz pública, análise e eliminação automática.

## Testes a prever
1. Nominal: Enviar um ficheiro válido e encontrá-lo do lado da administração.
2. Controlo de recusa: Um ficheiro demasiado pesado, disfarçado ou executável é recusado.
3. Invariante: Nenhum ficheiro enviado é executável nem servido diretamente ao público.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
