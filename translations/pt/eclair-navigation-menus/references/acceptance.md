# Plano de validação — Menus de navegação

## Modelo de dados
Menu, entrada, ordem, destino, localização.

## Implementação esperada
Limitar o menu principal aos percursos essenciais, arrumar o resto no rodapé, testar com teclado e em dispositivos móveis.

## Testes a prever
1. Nominal: Compor os menus e percorrê-los com o teclado e em dispositivos móveis.
2. Controlo de recusa: Uma página despublicada desaparece do menu ou é assinalada, nunca é servida em 404 a partir da navegação.
3. Invariante: Nenhuma ligação de menu aponta para um rascunho ou para um endereço externo não pretendido.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
