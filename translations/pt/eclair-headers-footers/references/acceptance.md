# Plano de validação — Cabeçalhos e rodapés

## Modelo de dados
Logótipo, menu, contactos, ligações legais.

## Implementação esperada
Passar por um pacote de tema em site/themes, respeitar as variáveis do contrato de tema, manter a ligação de salto e as ligações legais.

## Testes a prever
1. Nominal: Validar o tema e verificar o cabeçalho e o rodapé em todas as páginas-tipo.
2. Controlo de recusa: O tema recusado pelo validador não é entregue.
3. Invariante: Nunca gerar por conta própria etiquetas SEO ou cabeçalhos já fornecidos pelo núcleo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
