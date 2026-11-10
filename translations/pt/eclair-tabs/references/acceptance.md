# Plano de validação — Separadores

## Modelo de dados
Separador, título, painel.

## Implementação esperada
Construir um bloco de separadores com papéis ARIA, navegação com as setas e recurso a secções empilhadas.

## Testes a prever
1. Nominal: Percorrer os separadores com o teclado e com o leitor de ecrã.
2. Controlo de recusa: Sem JavaScript, todos os painéis estão visíveis.
3. Invariante: Todo o conteúdo permanece no HTML, logo legível sem JavaScript.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
