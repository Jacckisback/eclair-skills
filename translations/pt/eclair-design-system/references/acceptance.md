# Plano de validação — Sistema de design

## Modelo de dados
Tokens, grelha, espaçamentos, cores, tipografia, componentes e estados.

## Implementação esperada
Declarar a escala dos tokens, reutilizar componentes, documentar estados e variantes; compatibilidade com o tema Éclair.

## Testes a prever
1. Nominal: Testar o contraste, a coerência e a mudança de tema.
2. Controlo de recusa: Alterar a cor principal não cria nenhuma ilegibilidade das ligações ou dos erros.
3. Invariante: Não introduzir uma folha CSS pesada nem uma biblioteca JS sem prova de necessidade.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
